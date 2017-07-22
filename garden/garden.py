from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
def home_page():
    flora = mongo.db.flora.find()

    return render_template('index.html', flora=flora)

@app.route('/<binomial>')
def plant_page(binomial):
    plant = mongo.db.flora.find_one({"binomial": binomial})

    return render_template('plant.html', plant=plant)