from flask import Flask, render_template, url_for

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/quotes')
def quotes():
	return ""


@app.route('/quotes/<int:id>')
def specificQuote(id):
	return f"quote id: {id}"


@app.route('quotes/submit')
def submit():
	return ""


if __name__ == "__main__":
	app.run()
