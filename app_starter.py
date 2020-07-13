# imports
import numpy as np
import pandas as pd
import json
from flask import Flask, request, Response, flash, render_template, jsonify, url_for, redirect
from flask_table import Table, Col
from jinja2 import Template



# initialize the flask app
app = Flask('my_app')


info = json.load(open('assets/items.json', 'rb'))


# route 1: home page
@app.route('/')
def home():
    #return a simple string
    return render_template('image1.html')
                  


# route 2: show a form 
@app.route('/form')
def form():
    # use flask's render_template function to display an html page
    return render_template('form.html')


# route 3: accept the form submission
@app.route('/submit')
def submit():
    data = request.args
    
    suggestions = {key : info.get(key, 'Unfortunately we do not have your item in the database.') for key in data.values()}
       
    return render_template('results.html', prediction = suggestions, recommendations = list(suggestions.values())[0])
   


# Call app.run(debug=True) 
if __name__ == '__main__': # if you run `python app_starter.py` from terminal
    app.run(debug=True)
