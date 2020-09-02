from json_handler import GetJson, AddQuote


class Quote:
	def __init__(self, Quote, Source):
		self.Id = None
		self.Quote = Quote

		self.Source = {
			"Person": Source["Person"],
			"Episode": Source["Episode"]
		}

		self.SetId()

	def SetId(self):
		quote_list = GetJson()
		id_list = [quote["Id"] for quote in quote_list["quotes"]]

		highest_id = max(id_list)
		self.Id = highest_id + 1

	def SaveQuote(self):
		AddQuote(self)