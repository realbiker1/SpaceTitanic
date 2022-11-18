from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, BooleanField, SelectField
from wtforms.validators import DataRequired, NumberRange

class DataForm(FlaskForm):

    age = IntegerField('Please enter age', validators=[NumberRange(min=0, max=99, message="Age must be between 0 and 99"), DataRequired(message="Age is required")])
    cryosleep = BooleanField(label='Did you enter cryosleep during the trip?', validators=[DataRequired(message="Please check if you want to cryosleep")])
    vrdeck = IntegerField('How much did you spend on the VRDeck', validators=[NumberRange(min=0, max=1000000, message="Value must be between 0 and 1000000")])
    spa = IntegerField('How much did you spend on the ships spa', validators=[NumberRange(min=0, max=1000000, message="Value must be between 0 and 1000000")])
    shoppingmall = IntegerField('How much did you spend on the shopping mall', validators=[NumberRange(min=0, max=1000000, message="Value must be between 0 and 1000000")])
    roomservice = IntegerField('How much did you spend on roomservice', validators=[NumberRange(min=0, max=1000000, message="Value must be between 0 and 1000000")])
    homeplanet = SelectField('What is your home planet?', choices=[('Earth'), ('Europa'), ('Mars')], validators=[DataRequired(message="Please select a homeplanet")])
    destination = SelectField('What is your destination?', choices=[('TRAPPIST-1e'), ('55 Cancri e'), ('PSO J318.5-22')], validators=[DataRequired(message="Please select a destination")])
    groupsize = IntegerField('How many people are you travelling with 0-10?', validators=[NumberRange(min=0, max=10, message="Value must be between 0 and 10"), DataRequired(message="Age is required")])

    submit = SubmitField('Submit')