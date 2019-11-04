from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, FloatField
from wtforms import validators


class VendorFormEdit(FlaskForm):
    vendor_name = HiddenField("name:")

    vendor_balance = FloatField("Balance: ", [
        validators.DataRequired("Please, enter balance."),
        validators.Length(1, 15, "Balance should be from 1 to 15 symbols, >0")])

    vendor_country = StringField("Country: ", [
        validators.DataRequired("Please, enter country."),
        validators.Length(2, 20, "Country should be from 2 to 20 symbols")
    ])

    vendor_city = StringField("City: ", [
        validators.DataRequired("Please, enter city."),
        validators.Length(3, 9, "City should be from 3 to 9 symbols")
    ])

    submit = SubmitField("Save")
