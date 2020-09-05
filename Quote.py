from json_handler import GetJson, SetJson


class Source:
	def __init__(self, person, episode):
		self.Person = person
		self.Episode = episode


class Quote:
	def __init__(self, quote, source, id=None):
		self.Id = id
		self.Quote = quote

		self.Source = source

		if self.Id is None:
			self.SetId()

	def SetId(self):
		quote_list = GetJson()
		id_list = [quote["Id"] for quote in quote_list["quotes"]]

		highest_id = max(id_list)
		self.Id = highest_id + 1

	def Save(self):
		new_quote = {
			"Id": self.Id,
			"Quote": self.Quote,
			"Source": {
				"Person": self.Source.Person,
				"Episode": self.Source.Episode
			}
		}

		structure = GetJson()
		structure["quotes"].append(new_quote)

		SetJson(structure)

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
