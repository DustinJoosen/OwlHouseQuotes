import sys
import json

#the standard path for the quotes#
fp = "static/json/quotes.json"


#returns a list of json in the filepath, when not specified it chooses the quotes#
def GetJson(path=fp):
	try:
		with open(path, 'r') as file:
			data = json.load(file)
	except:
		sys.exit()
	finally:
		return data


#sets the json to the specified filepath#
def SetJson(structure, path=fp):
	try:
		with open(path, 'w') as file:
			file.write(json.dumps(structure, indent=4))
	except:
		sys.exit()
