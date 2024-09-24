# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # ... initiationg app to flask with name

@app.route("/")                # ... routes the file
def hello_world():
    print(__name__)            # ... function that prints the name of the flask
    return "No hablo queso!"   # ... returns spanish string

app.run()                      # ... runs the file

# returns a warning and the location of the http(?) and the site returns the return string              