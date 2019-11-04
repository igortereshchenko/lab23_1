from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms import validators


class VendorForm(FlaskForm):
    vendor_name = StringField()

    vendor_balance = FloatField("Vendor Balance: ", [
        validators.DataRequired("Please, enter balance."),
        validators.Length(1, 15, "Balance should be from 1 to 15 symbols, >0")
    ])

    vendor_country = StringField("Recommendation Country: ", [
        validators.DataRequired("Please, enter country."),
        validators.Length(2, 20, "Country should be from 2 to 20 symbols")
    ])

    vendor_city = StringField("Vendor City: ", [
        validators.DataRequired("Please, enter city."),
        validators.Length(3, 9, "City should be from 3 to 9 symbols")
    ])


    submit = SubmitField("Save")