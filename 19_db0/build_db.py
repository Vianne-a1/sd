#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


with open("students.csv") as students_csv:
    reader = csv.DictReader(students_csv)  
    for row in reader:
        c.execute("INSERT INTO students (id, name) VALUES (?, ?)", (row['id'], row['name']))


with open("courses.csv") as courses_csv:
    reader = csv.DictReader(courses_csv)  
    for row in reader:
        c.execute("INSERT INTO courses (code, mark, id) VALUES (?, ?, ?)", 
                  (row['code'], row['mark'], row['id']))


command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
