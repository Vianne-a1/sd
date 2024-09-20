# Tiffany Yang, Chloe Wong, Claire Song
# Team X
# SoftDev
# K05 -- Adding more info to lists/dicts
# 2024-09-17
# time spent: 1 hour

import random

occupations = []  

def createList():
    with open("06_py-csv/occupations.csv", "r") as file:
        data = file.read().split("\n")
        for job in data:
            percent= job.split(",")
            occupations.append({"job": percent[0]})

def pickJob():
    createList()  
    if len(occupations) == 0:
        print("The list is empty!")
        return
    l = int(len(occupations)//2 - 1)
    choice = random.randint(0, l)
    job= occupations[choice]
    print(job)

pickJob()
