from flask import Flask, render_template, request
from mediSell import app
from query_results import query_results
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.fields import RadioField, SubmitField, SelectField, TextField
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
import psycopg2

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    city  = request.form['inputcity']
    specialty  = request.form['specialtyselect']
    city = city.upper()
    specialty = specialty.upper()
    results = query_results(city,specialty)
    return render_template("index.html",classes=results)
