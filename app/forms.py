from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    """
    The form for entering values during patient encounter. Feel free to add additional 
    fields for the remaining features in the data set (features missing in the form 
    are set to default values in `predict.py`).
    """

    PassengerId = object('A unique Id for each passenger.')
    HomePlanet = object('The planet the passenger departed from')

    CryoSleep = object('Indicates if the passenger is "sleeping" in their cabins')
    Cabin = object('The cabin number where the passenger is staying')

    Destination = object('The planet the passenger will be debarking to.')
    Age = FloatField('The age of the passenger', validators=[DataRequired()])
    VIP = object('Wheter the passenger has paid for special VIP service during the voyage')
    RoomService, Foodcourt, ShoppingMall, Spa, VRDeck = FloatField('Amount the passenger has billed these luxury amenities', validators=[DataRequired()])
    Name = object('The first and last names of the passenger')
    Transported = BooleanField(label='Transported')



    submit = SubmitField('Submit')