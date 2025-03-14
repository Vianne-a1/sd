from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.executescript('''
    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS blogs;
    DROP TABLE IF EXISTS entries;

    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );

    CREATE TABLE blogs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    );

    CREATE TABLE entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        blog_id INTEGER NOT NULL,
        content TEXT NOT NULL,
        FOREIGN KEY (blog_id) REFERENCES blogs (id)
    );
    ''')
    conn.close()

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        conn = get_db_connection()
        g.user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()

@app.route('/')
def index():
    if g.user:
        return redirect(url_for('home'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if user and check_password_hash(user['password'], password):
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/home')
def home():
    if not g.user:
        return redirect(url_for('login'))
    conn = get_db_connection()
    blogs = conn.execute('SELECT * FROM blogs WHERE user_id = ?', (g.user['id'],)).fetchall()
    conn.close()
    return render_template('home.html', blogs=blogs)

@app.route('/new_blog', methods=['GET', 'POST'])
def new_blog():
    if not g.user:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = get_db_connection()
        conn.execute('INSERT INTO blogs (user_id, title, content) VALUES (?, ?, ?)', (g.user['id'], title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template('new_blog.html')

@app.route('/add_entry/<int:blog_id>', methods=['GET', 'POST'])
def add_entry(blog_id):
    if not g.user:
        return redirect(url_for('login'))
    if request.method == 'POST':
        content = request.form['content']
        conn = get_db_connection()
        conn.execute('INSERT INTO entries (blog_id, content) VALUES (?, ?)', (blog_id, content))
        conn.commit()
        conn.close()
        return redirect(url_for('view_blog', blog_id=blog_id))
    return render_template('add_entry.html', blog_id=blog_id)

@app.route('/view_blog/<int:blog_id>')
def view_blog(blog_id):
    if not g.user:
        return redirect(url_for('login'))
    conn = get_db_connection()
    blog = conn.execute('SELECT * FROM blogs WHERE id = ?', (blog_id,)).fetchone()
    entries = conn.execute('SELECT * FROM entries WHERE blog_id = ?', (blog_id,)).fetchall()
    conn.close()
    return render_template('view_blog.html', blog=blog, entries=entries)

@app.route('/edit_entry/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    if not g.user:
        return redirect(url_for('login'))
    conn = get_db_connection()
    entry = conn.execute('SELECT * FROM entries WHERE id = ?', (entry_id,)).fetchone()
    if request.method == 'POST':
        content = request.form['content']
        conn.execute('UPDATE entries SET content = ? WHERE id = ?', (content, entry_id))
        conn.commit()
        conn.close()
        return redirect(url_for('view_blog', blog_id=entry['blog_id']))
    conn.close()
    return render_template('edit_entry.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)