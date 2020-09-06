from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


persons = ["Eda", "Luz", "King", "Amity", "Willow", "Guz/Augustus", "Lilith", "Other"]
episodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


class SubmitQuoteForm(FlaskForm):
	quote = StringField("Quote", validators=[DataRequired()])
	source_person = SelectField("Said by", choices=persons, validators=[DataRequired()])
	source_episode = SelectField("In episode: ", choices=episodes, validators=[DataRequired()])
	submit = SubmitField("Send")
