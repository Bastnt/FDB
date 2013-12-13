class Wrapper:
	def __init__(self, name):
		self.name = name

	def execute(self, req):
		print("\nWhat {} executes: ".format(self.name))
		print("SELECT ", end="")
		for p in req.projection:
			print(p, end=", ")
		print(" WHERE "+req.selection)