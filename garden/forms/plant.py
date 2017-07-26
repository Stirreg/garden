from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PlantForm(FlaskForm):
    """Plant form."""
    binomial = StringField('binomial', validators=[validators.DataRequired()])
    names = StringField('names', validators=[validators.DataRequired()])
    cultivars = StringField('cultivars', validators=[validators.Optional()])
