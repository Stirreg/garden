import os
import base64
from flask import Flask
from flask_pymongo import PyMongo
from garden.repositories.plant import PlantRepository
from garden.services.plant import PlantService

app = Flask(__name__)

app.config.from_object('config.default')
app.config.from_object(os.getenv('APP_CONFIG'))

mongo = PyMongo(app)

plant_repository = PlantRepository(mongo)

plant_service = PlantService(plant_repository)


@app.template_filter('b64encode')
def b64encode(string):
    return base64.b64encode(string).decode('utf-8')


import garden.views.plant  # noqa: E402, F401
