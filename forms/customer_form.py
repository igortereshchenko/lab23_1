from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms import validators


class CreateCustomer(FlaskForm):
    name = StringField("Name: ", [
        validators.DataRequired("Please enter your Name.")

    ])
    email = StringField("Email: ", [
        validators.DataRequired("Please enter your Email.")
        , validators.Email("Please enter correct Email.")
    ])
    phone = IntegerField("Phone: ", [
        validators.DataRequired("Please enter your Phone.")

    ])

    birthday = DateField("Birthday: ", [
        validators.DataRequired("Please enter your Birthday.")

    ])

    submit = SubmitField("Save")
