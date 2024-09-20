# Tiffany Yang, Chloe Wong, Claire Song
# Team X
# SoftDev
# K05 -- Adding more info to lists/dicts
# 2024-09-17
# time spent: 1 hour

# Tiffany Yang, Chloe Wong, Claire Song
# Team X
# SoftDev
# K05 -- Adding more info to lists/dicts
# 2024-09-17
# time spent: 1 hour

import csv
import random

occupations = []  
weights = []

def createList():
    with open("/home/students/odd/2025/tyang50/Downloads/occupations.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row:  # Check if row is not empty
                job = row[0]
                weight = float(row[1])  # Convert percentage to float
                occupations.append(job)
                weights.append(weight)
        occupations.remove(len(occupations)-1)
        weights.remove(len(weights)-1)
def pickJob():
    createList()  
    if len(occupations) == 0:
        print("The list is empty!")
        return
    job = random.choices(occupations, weights=weights, k=1)[0]
    print(job)
    
pickJob()
                                                                                                                        
