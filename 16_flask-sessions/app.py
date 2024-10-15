'''
Tiffany Yang, Chloe Wong, Claire Song
Topher Forever
SoftDev
K16
2024-10-08
time spent: 1 hr
'''
from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

team_name = "Topher Forever"
roster = ["Tiffany Yang", "Chloe Wong", "Claire Song"]

@app.route('/')
def index():
    return render_template('login.html', team_name=team_name, roster=roster)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        username = request.form.get('username')
    else:
        username = request.args.get('username')
    
    greeting = f"Hello, {username}! Welcome to our beautiful Flask App!"
    session['username'] = username  # Save username to session

    # Explanation of GET vs POST
    explanation = """
    GET: Sends data via the URL (useful for retrieving information).
    POST: Sends data through the body (useful for modifying server-side data).
    In this Flask app:
    - GET: The username is passed via the URL.
    - POST: The username is passed via the form body.
    """
    
    return render_template(
        'response.html',
        username=username,
        method=request.method,
        greeting=greeting,
        explanation=explanation,
        team_name=team_name,
        roster=roster
    )

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)
