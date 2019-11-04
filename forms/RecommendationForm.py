from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms import validators


class RecommendationForm(FlaskForm):
    recommendation_id = IntegerField()

    recommendation_name = StringField("Recommendation Name: ", [
        validators.DataRequired("Please, enter name."),
        validators.Length(3, 15, "Name should be from 3 to 15 symbols")
    ])

    recommendation_model = StringField("Recommendation Model: ", [
        validators.DataRequired("Please, enter model."),
        validators.Length(2, 20, "Model should be from 2 to 20 symbols")
    ])

    recommendation_price = FloatField("Recommendation Price: ", [
        validators.DataRequired("Please, enter price."),
        validators.Length(3, 9, "Price should be from 3 to 9 symbols")
    ])


    submit = SubmitField("Save")