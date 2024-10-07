# Tiffany Yang
# SoftDev
# Sep 27 2024

from flask import Flask, render_template, jsonify
import random
import csv

app = Flask(__name__) #jibili

@app.route("/")
def hello_world():
    return "No hablo queso!"

def numbercruncher():
    list1 = []
    percentage = []
    job = []
    print("the __name__ of this module is... ")
    print(__name__)
    
    # Load the occupations data from CSV
    with open('occupations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list1.append(row)
    
    for dict1 in list1:
        percentage.append(float(dict1.get("Percentage")))
        job.append(dict1.get("Job Class"))

    # Remove the last entry (which is the "Total")
    job.pop()
    percentage.pop()

    # Return the job list and randomly selected job
    selected_occupation = random.choices(job, weights=percentage)[0]  # extract single occupation
    return {"selected_occupation": selected_occupation, "job_list": job}

title = "Occupation Selector"
desc = "Occupations and Random Selector"
roster = "TNPG + Chloe and Tiffany"

@app.route("/wdywtbwygp")
def idkwtsf():
    # Refresh the occupations and selected occupation on each load
    data = numbercruncher()
    selected_occupation = data["selected_occupation"]
    job_list = data["job_list"]
    
    return render_template('idkwtsf.html', 
                           title=title, 
                           desc=desc, 
                           roster=roster, 
                           selected_occupation=selected_occupation, 
                           job_list=job_list)

@app.route("/teams") 
def team():
    devos = ["Chloe Wong, "Tiffany Yang"]
    return render_template('team.html', teamName="Untitled", collection=devos)

@app.route("/my_foist_template") 
def test_tmplt():
    coll = [0,1,1,2,3,5,8]
    return render_template('model_tmplt.html', foo="fooooo", collection=coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
