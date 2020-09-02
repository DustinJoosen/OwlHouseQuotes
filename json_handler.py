import json

fp = "static/quotes.json"


def GetJson():
	with open(fp, 'r') as file:
		data = json.load(file)

	return data


def SetJson(structure):
	with open(fp, 'w') as file:
		json.dump(file, structure)


def AddQuote(quote):
	new_quote = {
		"Id": quote.Id,
		"Quote": quote.Quote,
		"Source":{
			"Person": quote["Person"],
			"Episode": quote["Episode"]
		}
	}

	structure = GetJson()
	structure["quotes"].Append(new_quote)

	SetJson(structure)
