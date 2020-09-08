from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from json_handler import GetJson


persons = ["Eda", "Luz", "King", "Amity", "Willow", "Guz/Augustus", "Lilith", "Other"]
episodes = GetJson("static/json/episodes.json")["episodes"]


class SubmitQuoteForm(FlaskForm):
	quote = StringField("Quote", validators=[DataRequired()])
	source_person = SelectField("Said by", choices=persons, validators=[DataRequired()])
	source_episode = SelectField("In episode: ", choices=episodes, validators=[DataRequired()])
	submit = SubmitField("Send")
