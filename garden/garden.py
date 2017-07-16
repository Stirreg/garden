from flask import Flask, render_template
from flask_pymongo import PyMongo
from wikipedia import wikipedia

app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/')
def home_page():    
    flora = list(mongo.db.flora.find())

    for plant in flora:
        plant['image'] = wikipedia.page(plant['binomial']).images[0]

    return render_template('index.html', flora=flora)