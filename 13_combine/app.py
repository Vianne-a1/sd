# Tiffany Yang
# SoftDev
# Sep 27 2024

from flask import Flask, render_template
import random
app = Flask(__name__) #jibili

@app.route("/")
def hello_world():
    return "No hablo queso!"

title = "title"
desc = "heading"
roster = "TNPG + Chloe and Tiffany"
randomjob = random.choices(job, weights=percentage)
table = "filler"


@app.route("/wdywtbwygp")
def idkwtsf():
    return render_template('idkwtsf.html', title = title, desc = heading, roster= roster, randomjob = job, table = table)


'''    * an appropriate title,
   * a descriptive heading,
   * TNPG+roster,
   * and a tablified version of the occupations data, along with
   * a randomly selected occupation shown at the top (each page refresh should yield a newly-chosen occupation).'''

@app.route("/teams") 
def team():
    return render_template('team.html', teamName="Untitled", collection=devos)


@app.route("/my_foist_template") 
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)



if __name__ == "__main__":
    app.debug = True
    app.run()