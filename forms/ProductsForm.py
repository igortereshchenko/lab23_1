from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import validators


class ProductsForm(FlaskForm):
    product_id = IntegerField()

    product_name = StringField("Name: ", [
        validators.DataRequired("Please, enter product's name."),
        validators.Length(3, 15, "Product's name should be from 3 to 15 symbols")])

    product_model = StringField("Model: ", [
        validators.DataRequired("Please, enter product's model."),
        validators.Length(2, 20, "Product's model should be from 2 to 20 symbols")
    ])

    submit = SubmitField("Save")