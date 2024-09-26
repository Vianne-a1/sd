# Tiffany Y
# SoftDev
# September 2024

from flask import Flask, jsonify
import random
import csv


app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
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


if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()