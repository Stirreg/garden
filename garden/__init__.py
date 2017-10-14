from flask import Flask
from flask_pymongo import PyMongo
from garden.repositories.plant import PlantRepository

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MONGO_CONNECT'] = False
app.config['MONGO_HOST'] = '0.0.0.0'

mongo = PyMongo(app)

plant_repository = PlantRepository(mongo)

import garden.views.plant
