"""Garden module."""
from garden import app
from flask import Flask, render_template, request, redirect, url_for, abort
from flask_pymongo import PyMongo
from garden.forms.plant import PlantForm
from bson import Binary
import base64

# TODO: Refactor EVERYTHING!

mongo = PyMongo(app)

app.secret_key = 'very-secret-key'

#class Plant():

#    def __init__(self, binomial, names, cultivars):
#        self.binomial = binomial
#        self.names = names
#        self.cultivars = cultivars


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
        data['binomial'] = form.binomial.data
        data['names'] = form.names.data.split(', ')

        if form.cultivars.data:
            data['cultivars'] = form.cultivars.data.split(', ')

        if form.image.data:
            data['image'] = Binary(form.image.data.read())

        mongo.db.flora.update_one(
            {'binomial': data['binomial']},
            {'$set': data}
        )

        return redirect(url_for('home_page') + '#' + data['binomial'])

    plant = mongo.db.flora.find_one({'binomial': binomial})

    if not plant:
        abort(404)

    return render_template('plant.html', plant=plant, form=form)


@app.route('/plant', methods=('GET', 'POST'))
def create_plant_page():
    """Create plant page method"""
    form = PlantForm()
    if request.method == 'POST' and form.validate():
        data = {}
        data['binomial'] = form.binomial.data
        data['names'] = form.names.data.split(', ')
        if form.cultivars.data:
            data['cultivars'] = form.cultivars.data.split(', ')

        mongo.db.flora.insert_one(data)

        return redirect(url_for('home_page') + '#' + data['binomial'])

    return render_template('plant.html', form=form)


@app.route('/plant/delete/<binomial>')
def delete_plant(binomial):
    """Delete plant method."""
    mongo.db.flora.delete_one({'binomial': binomial})

    return redirect(url_for('home_page'))
