from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.fields.html5 import DateTimeLocalField


class SearchForm(FlaskForm):
    """ Search form for main page """

    location = SelectField('Location')
    pick_up_date = DateTimeLocalField("Pick-up date", format="%Y-%m-%dT%H:%M")
    drop_off_date = DateTimeLocalField("Drop-off date", format="%Y-%m-%dT%H:%M")
    submit = SubmitField('Search')
