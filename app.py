from flask import Flask, render_template, url_for
from Quote import Quote, Source

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/quotes')
def quotes():
	quotes_list = Quote.GetQuotes()
	return render_template('quote_list.html', quotes=quotes_list)


@app.route('/quotes/<int:id>')
def specificQuote(id):
	return render_template('specific_quote.html')


@app.route('/quotes/submit')
def submit():
	return render_template('submit_quote.html')


if __name__ == "__main__":
	app.run()
