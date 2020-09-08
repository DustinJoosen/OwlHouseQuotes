from flask import Flask, render_template, redirect, request
from Quote import Quote, Source
from Forms import SubmitQuoteForm
import random

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "blight_sexual"


@app.route('/')
def index():
	quotes_list = Quote.GetQuotes()
	random_quote = quotes_list[random.randint(0, len(quotes_list) - 1)]

	return render_template('index.html', quote=random_quote)


@app.route('/quotes')
def quotes():
	quotes_list = Quote.GetQuotes()
	return render_template('quote_list.html', quotes=quotes_list)


@app.route('/quotes/<int:id>')
def specificQuote(id):
	quotes_list = Quote.GetQuotes()
	for quote in quotes_list:
		if quote.Id == id:
			quote = Quote(quote.Quote, quote.Source, quote.Id)
			return render_template("specific_quote.html", quote=quote)


@app.route('/quotes/submit', methods=["POST", "GET"])
def submit():
	form = SubmitQuoteForm()
	if form.validate_on_submit():
		try:
			quote = form.quote.data
			episode = form.source_episode.data
			person = form.source_person.data
		except:
			return render_template("submit_quote.html", form=form)

		specific_person = request.form["source_person_other"]
		if specific_person != "":
			person = specific_person

		quote = Quote(quote, Source(person, episode))
		quote.Save()

		return redirect('/quotes')

	return render_template('submit_quote.html', form=form)


if __name__ == "__main__":
	app.run()
