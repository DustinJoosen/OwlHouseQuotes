from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class SubmitQuoteForm(FlaskForm):
	quote = StringField("Quote", validators=[DataRequired()])
	source_person = StringField("Said by: ", validators=[DataRequired()])
	source_episode = StringField("In episode: ", validators=[DataRequired()])
	submit = SubmitField("Send")
