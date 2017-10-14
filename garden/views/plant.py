"""Garden module."""
import base64
from bson import Binary
from garden.models.plant import Plant
from garden.forms.plant import PlantForm
from garden import app, mongo, plant_repository
from flask import Flask, render_template, request, redirect, url_for, abort

# TODO: More dependency injection plz.

app.secret_key = 'very-secret-key'

@app.template_filter('b64encode')
def b64encode(string):
    return base64.b64encode(string).decode('utf-8')


@app.route('/')
def home_page():
    """Plant page view method."""
    flora = plant_repository.get_all()

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

        plant_repository.save(plant)

        return redirect(url_for('home_page') + '#' + plant.binomial)

    plant = plant_repository.get_one_by_binomial(binomial)

    if not plant:
        abort(404)

    return render_template('plant.html', plant=plant, form=form)


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

        plant_repository.save(plant)

        return redirect(url_for('home_page') + '#' + plant.binomial)

    return render_template('plant.html', form=form)


@app.route('/plant/delete/<binomial>')
def delete_plant(binomial):
    """Delete plant method."""
    plant_repository.delete_one_by_binomial(binomial=binomial)

    return redirect(url_for('home_page'))
