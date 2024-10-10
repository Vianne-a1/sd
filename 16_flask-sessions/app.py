'''
Tiffany Yang, Chloe Wong, Claire Song
Topher Forever
SoftDev
K16
2024-10-08
time spent: 1 hr
'''
from flask import Flask, render_template, request

app = Flask(__name__)

team_name = "X"
roster = ["Tiffany Yang, Chloe Wong, Claire Song"]

@app.route('/')
def index():
    return render_template('login.html', team_name=team_name, roster=roster)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    username = request.args.get('username') if request.method == 'GET' else request.form.get('username')
    method_used = request.method
    greeting = f"Hello, {username}! Welcome to our beautiful Flask App!"
    return render_template('response.html', username = username, method_used= method_used, greeting= greeting)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('logout.html')


    #explaining get vs post
    explanation = """
    GET: Sends data via the URL (useful for retrieving information).
    POST: Sends data through the body (useful for modifying server-side data).
    In this Flask app:
    - GET: The username is passed via the URL.
    - POST: The username is passed via the form body.
    """
    
    return render_template('response.html', username=username, method=method_used, greeting=greeting, explanation=explanation, team_name=team_name, roster=roster)

if __name__ == '__main__':
    app.run(debug=True)
