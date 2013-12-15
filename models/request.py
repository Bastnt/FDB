class Req:
	def __init__(self, projection = [], selection = "", table = ""):
		self.projection = projection
		self.selection = selection
		self.table = table