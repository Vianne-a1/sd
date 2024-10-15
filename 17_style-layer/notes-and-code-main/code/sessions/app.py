""" simple all-in-one flask app with session handling
"""

#adapted from
# https://flask.palletsprojects.com/en/3.0.x/quickstart/#sessions


from flask import Flask
from flask import session
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'qwrqwsxolwcbuytr_5#y2L"ujedcF4Qsdfastiugyhkb8z\nasdf\xecgb;lkiy]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
