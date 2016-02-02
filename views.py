from flask import Flask, render_template, request
from mediSell import app
from query import query_results
from flask_wtf import Form
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/createtable', methods=['GET','POST'])
def createtable():
    print request.form
    city  = request.form['city']
    specialty  = request.form['specialty']
    city = city.upper()
    #specialty = specialty.upper()
    results = query_results(city,specialty)
    class_results=results['class_list']
    return render_template("createtable.html",drugclasses=class_results)
