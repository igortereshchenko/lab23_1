from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, FloatField
from wtforms import validators


class RecommendationFormEdit(FlaskForm):
    recommendation_id = HiddenField("id:")

    recommendation_name = StringField("Name: ", [
        validators.DataRequired("Please, enter name."),
        validators.Length(3, 15, "Product's name should be from 3 to 15 symbols")])

    recommendation_model = StringField("Model: ", [
        validators.DataRequired("Please, enter model."),
        validators.Length(2, 20, "Product's model should be from 2 to 20 symbols")
    ])

    recommendation_price = FloatField("Price: ", [
        validators.DataRequired("Please, enter price."),
        validators.Length(3, 9, "Price should be from 3 to 9 symbols")
    ])

    submit = SubmitField("Save")
