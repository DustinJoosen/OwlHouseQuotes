from json_handler import GetJson, AddQuote


class Quote:
	def __init__(self, quote, source, id=None):
		self.Id = id
		self.Quote = quote

		self.source = {
			"Person": source["Person"],
			"Episode": source["Episode"]
		}

		if self.Id is None:
			self.SetId()

	def SetId(self):
		quote_list = GetJson()
		id_list = [quote["Id"] for quote in quote_list["quotes"]]

		highest_id = max(id_list)
		self.Id = highest_id + 1

	def Save(self):
		AddQuote(self)
