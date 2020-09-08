import sys
import json

fp = "static/json/quotes.json"


def GetJson(path=fp):
	try:
		with open(path, 'r') as file:
			data = json.load(file)
	except:
		sys.exit()
	finally:
		return data


def SetJson(structure, path=fp):
	try:
		with open(path, 'w') as file:
			file.write(json.dumps(structure, indent=4))
	except:
		sys.exit()
