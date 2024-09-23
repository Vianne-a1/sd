'''
Ben Rudinski
Novillo
SoftDev
K08: Flask Questions
2024-09-21
time spent: 1
'''

'''
DISCO:

Running the script prints the locally hosted website URL. Entering the URL brings us to a webpage that has the specified text printed out.

QCC:
0. What is flask?

Flask is a python framework that allows for python to be used on browser back-end.

1. Why do we need flask?

Flask is needed to handle site back-end operations.

2. Why was it named flask?

The previous framework was named bottle, so to with some wordplay, the new one was named flash.

3. Will we ever use flask in this class?

Yes, we just did on Friday.

4. Who created flask, in what year?

2004 by Pocoo, lead by Armin Ronacher

5. Are there any alternatives to flask?

Javascript and node.js?
 ...

INVESTIGATIVE APPROACH:
We set about this task by finding points of reference to understand what each function/terminology meant. 
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

# The maih function in python has simillar synthax with if "__name__"

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?

#  Could be a file path, also I see an @ symbol so it could be ran in terminal. Perhaps its the route of a path or website/application

def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?

 # It will print to the terminal/constole and it will print __main__
 
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

# It will enter in the browser when you enter the app route "/". This is because flask's routing system send the return value of the function as an HTTP request

app.run()                                # Q5: Where have you seen similar constructs in other languages?

# This looks like common java functions or processing functions

