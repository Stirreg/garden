"""Garden plant form module."""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, validators


class PlantForm(FlaskForm):
    """Plant form."""
    binomial = StringField('binomial', validators=[validators.DataRequired()])
    names = StringField('names', validators=[validators.DataRequired()])
    cultivars = StringField('cultivars', validators=[validators.Optional()])
    image = FileField(
        'image',
        validators=[
            FileAllowed(['jpg'], 'JPEG images only!')
        ]
    )
