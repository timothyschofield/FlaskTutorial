"""
12 October 2023

prob1 : python not found in terminal i.e. python --version does not work
    Go to Command palette Python: Select Interpreter
python --version still not work

prob2: Create a virtual environment
    Manage > Command prompt... Python Create Enviroment
    This appears to work - but pip (which is in the .venv > Lib) is still unknown

prob3: Activate the virtual environment
    In the terminal, navigate to the folder (probably the project folder) 
    that contains the .venv folder
    In the terminal .venv\Scripts\activate
==============================================================

Run the app by entering 
    python -m flask run
in the terminal

Naivgate to
    http://127.0.0.1:5000
or
    http://127.0.0.1:5000/hello/Tim

"""

import re
from datetime import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)

# http://127.0.0.1:5000/hello/Tim

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template("hello_there.html", name = name, date = datetime.now())
  
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json") # Not rendered

