# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import request
from flask import send_file
import os
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/inputdata', methods = ['POST'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    with open('data.json', 'w') as f:
        f.write(request.data.decode('utf-8'))
    os.system("python jsonparser.py")
    return 'Hello World'
    
@app.route('/', methods = ['GET'])
# ‘/’ URL is bound with hello_world() function.
def func():
    print(request.data)
    return send_file("index.html")

@app.route('/prediction', methods = ['GET'])
# ‘/’ URL is bound with hello_world() function.
def func5():
    print(request.data)
    return send_file("demofile.json")

# @app.route('/<path>', methods = ['GET'])
# def get():
#     return send_file(path)
 
@app.route('/bundle.d315eebd2f4cadc09885.js', methods = ['GET'])
# ‘/’ URL is bound with hello_world() function.
def f():
    print(request.data)
    return send_file("bundle.d315eebd2f4cadc09885.js")  

@app.route('/bundle.d315eebd2f4cadc09885.js.map', methods = ['GET'])
# ‘/’ URL is bound with hello_world() function.
def fr():
    print(request.data)
    return send_file("bundle.d315eebd2f4cadc09885.js.map") 

@app.route('/main.css', methods = ['GET'])
# ‘/’ URL is bound with hello_world() function.
def fu():
    print(request.data)
    return send_file("main.css")
 
@app.route('/skema4.glb', methods = ['GET'])
# ‘/’ URL is bound with hello_world() function.
def fuc():
    print(request.data)
    return send_file("skema4.glb")
  
@app.route('/main.css.map', methods = ['GET'])
# ‘/’ URL is bound with hello_world() function.
def fucn():
    print(request.data)
    return send_file("main.css.map")
 
 # main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()