from json_handler import GetJson, SetJson


#used to prevent magic strings, and cleaner code in general
class Source:
	def __init__(self, person, episode):
		self.Person = person
		self.Episode = episode


#used to retrieve data easier#
class Quote:
	def __init__(self, quote, source, id=None):
		self.Id = id
		self.Quote = quote

		self.Source = source

		#if the id is not set, create a new one#
		if self.Id is None:
			self.SetId()

	#sets a unique id(the highest one + 1)
	def SetId(self):
		quote_list = GetJson()
		id_list = [quote["Id"] for quote in quote_list["quotes"]]

		highest_id = max(id_list)
		self.Id = highest_id + 1

	#saves the current object to the json file#
	def Save(self):
		#makes an object, later to be turned into json#
		new_quote = {
			"Id": self.Id,
			"Quote": self.Quote,
			"Source": {
				"Person": self.Source.Person,
				"Episode": self.Source.Episode
			}
		}

		#retrieves json and add to it#
		structure = GetJson()
		structure["quotes"].append(new_quote)

		#saves the new json data
		SetJson(structure)

	#project wide method used to get a list of all the quotes, formatted to be objects of Quote#
	@staticmethod
	def GetQuotes():
		quote_list = []

		for quote in GetJson()["quotes"]:
			quote_list.append(Quote(
				quote=quote["Quote"],
				source=quote["Source"],
				id=quote["Id"])
			)

		return quote_list
