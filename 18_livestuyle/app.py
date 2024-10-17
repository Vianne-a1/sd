# Chloe Wong, Tiffany Yang, Claire Song
# Team X
# SoftDev
# K17 - opening HTML/CSS in flask app
# 2024-10-16
# Time Spent: 0.1 hr

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', style='static/style.css')

if __name__ == "__main__":
    app.debug = True
    app.run()