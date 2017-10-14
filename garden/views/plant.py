"""Garden module."""
import base64
from garden import app
from bson import Binary
from flask_pymongo import PyMongo
from garden.models.plant import Plant
from garden.forms.plant import PlantForm
from garden.repositories.plant import PlantRepository
from flask import Flask, render_template, request, redirect, url_for, abort

# TODO: Refactor EVERYTHING!

mongo = PyMongo(app)

app.secret_key = 'very-secret-key'

plantRepository = PlantRepository(mongo)

@app.template_filter('b64encode')
def b64encode(string):
    return base64.b64encode(string).decode('utf-8')


@app.route('/')
def home_page():
    """Plant page view method."""
    flora = mongo.db.flora.find().sort('names', 1)

    return render_template('index.html', flora=flora)


@app.route('/plant/<binomial>', methods=('GET', 'POST', 'DELETE'))
def plant_page(binomial):
    """Read and update plant page method."""
    form = PlantForm()
    if request.method == 'POST' and form.validate():
        data = {}

        if form.cultivars.data:
            data['cultivars'] = form.cultivars.data.split(', ')

        if form.image.data:
            data['image'] = Binary(form.image.data.read())

        plant = Plant(
            binomial=form.binomial.data,
            names=form.names.data.split(', ')
        )

        plantRepository.save(plant)

        return redirect(url_for('home_page') + '#' + plant.binomial)

    plant = plantRepository.get(binomial)

    if not plant:
        abort(404)

    return render_template('plant.html', plant=plant.__dict__, form=form)


@app.route('/plant', methods=('GET', 'POST'))
def create_plant_page():
    """Create plant page method"""
    form = PlantForm()
    if request.method == 'POST' and form.validate():
        data = {}

        if form.cultivars.data:
            data['cultivars'] = form.cultivars.data.split(', ')

        plant = Plant(
            binomial=form.binomial.data,
            names=form.names.data.split(', ')
        )

        plantRepository.save(plant)

        return redirect(url_for('home_page') + '#' + plant.binomial)

    return render_template('plant.html', form=form)


@app.route('/plant/delete/<binomial>')
def delete_plant(binomial):
    """Delete plant method."""
    mongo.db.flora.delete_one({'binomial': binomial})

    return redirect(url_for('home_page'))
