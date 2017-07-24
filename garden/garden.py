"""Garden module."""
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

# TODO: Refactor EVERYTHING!

app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def home_page():
    """Plant page view method."""
    flora = mongo.db.flora.find().sort('names', 1)

    return render_template('index.html', flora=flora)

@app.route('/plant/<binomial>', methods=('GET', 'POST', 'DELETE'))
def plant_page(binomial):
    """Read and update plant page method."""
    if request.method == 'POST':
        data = request.form.to_dict()

        if data['names']:
            data['names'] = data['names'].split(', ')
        if data['cultivars']:
            data['cultivars'] = data['cultivars'].split(', ')

        mongo.db.flora.update_one({'binomial': data['binomial']}, {'$set': data})

        return redirect(url_for('home_page') + '#' + data['binomial'])

    plant = mongo.db.flora.find_one({'binomial': binomial})

    return render_template('plant.html', plant=plant)

@app.route('/plant', methods=('GET', 'POST'))
def create_plant_page():
    """Create plant page method"""
    if request.method == 'POST':
        data = request.form.to_dict()

        if data['names']:
            data['names'] = data['names'].split(', ')
        if data['cultivars']:
            data['cultivars'] = data['cultivars'].split(', ')

        mongo.db.flora.insert_one(data)

        return redirect(url_for('home_page') + '#' + data['binomial'])

    return render_template('plant.html')

@app.route('/plant/delete/<binomial>')
def delete_plant(binomial):
    """Delete plant method."""
    mongo.db.flora.delete_one({'binomial': binomial})

    return redirect(url_for('home_page'))
