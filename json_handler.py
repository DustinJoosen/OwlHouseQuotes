import json

fp = "static/json/quotes.json"


def GetJson(path=fp):
	with open(path, 'r') as file:
		data = json.load(file)

	return data


def SetJson(structure, path=fp):
	with open(path, 'w') as file:
		file.write(json.dumps(structure, indent=4))
