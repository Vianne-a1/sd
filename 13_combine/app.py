# Tiffany Yang
# SoftDev
# Sep 27 2024

from flask import Flask, render_template
app = Flask(__name__) #jibili

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]
devos = ["Tracy Ye", "Tiffany Yang", "Chloe Wong"]

@app.route("/wdywtbwygp")
def idkwtsf():
    return numbercruncher + render_template('idkwtsf.html', title = title, desc = heading, roster= roster, randomjob = job, table = table)

def numbercruncher():
    list1=[]
    percentage=[]
    job=[]
    print("the __name__ of this module is... ")
    print(__name__)
    with open('occupations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list1.append(row)
    for dict1 in list1:
        percentage.append(float(dict1.get("Percentage")))
    for dict1 in list1:
        job.append(dict1.get("Job Class"))
    job.pop()
    percentage.pop()
    return jsonify({
        "team": "Jackie Zeng, Chloe Wong",
        "selected occupation": random.choices(job, weights=percentage),
        "occupations list": job})

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