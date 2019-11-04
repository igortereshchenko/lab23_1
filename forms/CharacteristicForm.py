from flask_wtf import Form
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms import validators


class CharacteristicForm(Form):
    characteristic_id = IntegerField()

    characteristic_specification = StringField("Specification: ", [
        validators.DataRequired("Please, enter your specification."),
        validators.Length(4, 15, "Specification should be from 4 to 15 symbols")
    ])

    characteristic_price = FloatField("Price: ", [
        validators.DataRequired("Please, enter price."),
        validators.Length(3, 9, "Price should be from 3 to 9 symbols")
    ])
    submit = SubmitField("Save")