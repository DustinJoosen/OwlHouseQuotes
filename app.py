from flask import Flask, render_template, redirect, request
from Quote import Quote, Source
from Forms import SubmitQuoteForm
import random

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "blight_sexual"


#the startup page, returns a view with a random quote#
@app.route('/')
def index():
	#gets a list of all quotes found, and selected a random one#
	quotes_list = Quote.GetQuotes()
	random_quote = quotes_list[random.randint(0, len(quotes_list) - 1)]

	#returns the standard view with the random quote as data#
	return render_template('index.html', quote=random_quote)


#returns a view with a list of all the quotes found#
@app.route('/quotes/')
@app.route('/quotes')
def quotes():
	#gets a list of all quotes, and return the list with the view#
	quotes_list = Quote.GetQuotes()
	return render_template('quote_list.html', quotes=quotes_list)


#returns a view with a specific quote, with the id of the parameter#
@app.route('/quotes/<int:id>/')
@app.route('/quotes/<int:id>')
def specificQuote(id):
	quotes_list = Quote.GetQuotes()

	#loop through all the quotes that have been found#
	for quote in quotes_list:
		#bascially checks if the quote is the one with the parameter id#
		if quote.Id == id:
			#create a new quote object, and give it to the view#
			quote = Quote(quote.Quote, quote.Source, quote.Id)
			return render_template("specific_quote.html", quote=quote)

	#when the parameter id is not being used, return to the list#
	return redirect(f'/quotes/')


#returns a view with a form where you can submit a new quote#
@app.route('/quotes/submit/', methods=["POST", "GET"])
@app.route('/quotes/submit', methods=["POST", "GET"])
def submit():
	form = SubmitQuoteForm()

	#when you submitted the form#
	if form.validate_on_submit():
		#tries to retrieve the basic data, on errors it reloads itself#
		try:
			quote = form.quote.data
			episode = form.source_episode.data
			person = form.source_person.data
		except:
			return render_template("submit_quote.html", form=form)

		#checks if the person has been set to 'Other'(if the textbox isn't empty),
		#if that is the case, change the person propertie to it's value
		specific_person = request.form["source_person_other"]
		if specific_person != "":
			person = specific_person

		#make a new quote object, not giving it a parameter and letting it know it's a new quote.
		#then save the quote in the json file#
		quote = Quote(quote, Source(person, episode))
		quote.Save()

		return redirect('/quotes')

	return render_template('submit_quote.html', form=form)


#when 404 errors happen, return a specific grid that helps you find the correct url#
@app.errorhandler(404)
def pageNotFound(e):
	return render_template("404.html", exception=e), 404


if __name__ == "__main__":
	app.run()
