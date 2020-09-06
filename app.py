from flask import Flask, render_template, url_for
from Quote import Quote, Source
import random

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
	quotes_list = Quote.GetQuotes()
	random_quote = quotes_list[random.randint(0, len(quotes_list) -1)]

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


@app.route('/quotes/submit')
def submit():
	return render_template('submit_quote.html')


if __name__ == "__main__":
	app.run()
