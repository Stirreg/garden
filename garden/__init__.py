import base64
from flask import Flask
from flask_pymongo import PyMongo
from garden.repositories.plant import PlantRepository
from garden.services.plant import PlantService

app = Flask(__name__)

app.jinja_env.auto_reload = True
app.secret_key = 'very-secret-key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MONGO_CONNECT'] = False
app.config['MONGO_HOST'] = '0.0.0.0'

mongo = PyMongo(app)

plant_repository = PlantRepository(mongo)

plant_service = PlantService(plant_repository)


@app.template_filter('b64encode')
def b64encode(string):
    return base64.b64encode(string).decode('utf-8')


import garden.views.plant
