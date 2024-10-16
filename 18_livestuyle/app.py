'''
Ben Rudinski
Topher Forever
SoftDev
K15: Intake -- Login and Response handling in flaask
2024-10-08
time spent: 1 hr
'''
from flask import Flask, render_template, request

app = Flask(__name__)

team_name = "Topher Forever"
roster = ["Ben Rudinski, Claire Song, Tiffany Yang"]

@app.route('/')
def index():
    return render_template('index.html', team_name=team_name, roster=roster)

    

if __name__ == '__main__':
    app.run(debug=True)