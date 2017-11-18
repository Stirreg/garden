'''Garden plant views module.'''
from garden.forms.plant import PlantForm
from garden import app, plant_service
from flask import render_template, request, redirect, url_for, abort


@app.route('/')
def home_page():
    '''Plant page view method.'''
    flora = plant_service.get_all()

    return render_template('index.html', flora=flora)


@app.route('/plant/<binomial>')
def plant_page(binomial):
    '''Plant detail method.'''
    plant = plant_service.get_one_by_binomial(binomial)

    if not plant:
        abort(404)

    return render_template('plant.html', plant=plant)

@app.route('/plant/edit/<binomial>', methods=('GET', 'POST', 'DELETE'))
def edit_plant_page(binomial):
    '''Edit plant page method.'''
    form = PlantForm()

    if request.method == 'POST' and form.validate():
        plant = plant_service.create_plant_from_form(form)
        plant_service.save_plant(plant)
        return redirect(url_for('home_page') + '#' + plant.binomial)

    plant = plant_service.get_one_by_binomial(binomial)

    if not plant:
        abort(404)

    return render_template('edit_plant.html', plant=plant, form=form)


@app.route('/plant', methods=('GET', 'POST'))
def create_plant_page():
    '''Create plant page method'''
    form = PlantForm()
    if request.method == 'POST' and form.validate():
        plant = plant_service.create_plant_from_form(form)
        plant_service.save_plant(plant)
        return redirect(url_for('home_page') + '#' + plant.binomial)

    return render_template('edit_plant.html', form=form)


@app.route('/plant/delete/<binomial>')
def delete_plant(binomial):
    '''Delete plant method.'''
    plant_service.delete_one_by_binomial(binomial=binomial)

    return redirect(url_for('home_page'))
