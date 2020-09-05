import json

fp = "static/quotes.json"


def GetJson():
	with open(fp, 'r') as file:
		data = json.load(file)

	return data


def SetJson(structure):
	with open(fp, 'w') as file:
		file.write(json.dumps(structure, indent=4))
