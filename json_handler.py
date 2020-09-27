import sys
import json


#returns a list of json in the filepath, when not specified it chooses the quotes#
def GetJson(path):
	try:
		with open(path, 'r') as file:
			data = json.load(file)
			return data
	except:
		sys.exit()


#sets the json to the specified filepath#
def SetJson(structure, path):
	try:
		with open(path, 'w') as file:
			file.write(json.dumps(structure, indent=4))
	except:
		sys.exit()
