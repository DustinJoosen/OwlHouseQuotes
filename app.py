from flask import Flask, render_template, redirect, request
from Quote import Quote, Source
from Forms import SubmitQuoteForm
from json_handler import GetJson
import random

settings = GetJson("static/json/app_settings.json")
pagenames = settings["pageNames"]

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = settings["secretKey"]


#the startup page, returns a view with a random quote#
@app.route('/')
@app.route('/random') 
def index():
	#gets a list of all quotes found, and selected a random one#
	quotes_list = Quote.GetQuotes()
	random_quote = quotes_list[random.randint(0, len(quotes_list) - 1)]

	#returns the standard view with the random quote as data#
	return render_template(pagenames["random"], quote=random_quote)


#returns a view with a list of all the quotes found#
@app.route('/quotes/')
@app.route('/quotes')
def quotes():
	#gets a list of all quotes, and return the list with the view#
	quotes_list = Quote.GetQuotes()
	return render_template(pagenames["list"], quotes=quotes_list)

	#TODO break the quote into multiple lines, when it becomes too long


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
			return render_template(pagenames["quote"], quote=quote)

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
			return render_template(pagenames["form"], form=form)

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

	return render_template(pagenames["form"], form=form)


#when 404 errors happen, return a specific grid that helps you find the correct url#
@app.errorhandler(404)
def pageNotFound(e):
	#TODO: add some more sad images in here
	sad_pictures = [
		"images/404/sad_luz.png",
		"images/404/crying_eda.png"
	]

	return render_template(pagenames["404"], path=random.choice(sad_pictures)), 404


if __name__ == "__main__":
	app.run()
