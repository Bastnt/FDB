# -*- coding: utf-8 -*-
from tree import *

# Request language
class Req:
	def __init__(self, projection = [], selection = ""):
		self.projection = projection
		self.selection = selection

# Dummy Wrapper
class Wrapper:
	def __init__(self, name):
		self.name = name

	def execute(self, req):
		print("\nWhat {} executes: ".format(self.name))
		print("SELECT ", end="")
		for p in req.projection:
			print(p, end=", ")
		print(" WHERE "+req.selection)

sql_wrapper = Wrapper("SQL")
xml_wrapper = Wrapper("XML")

def schema():
	# === XML example verified by this schema: ===
	# <Node:root>
	# 	<Node:team Leaf:id="1">
	# 		<Leaf:nom>Rocket</Leaf:nom>
	# 		<Leaf:age>22</Leaf:nom>
	# 	</Node:team>

	# 	<Node:team Leaf:id="2">
	# 		<Leaf:nom>Ash</Leaf:nom>
	# 		<Leaf:age>13</Leaf:nom>
	# 	</Node:team>
	# </Node:root>

	root = Node(None, "root")
	team = Node(root, "team")

	root.children.append(team)
	team.attributes.append(Attribute(team, "id", [sql_wrapper,xml_wrapper]))
	team.children.append(Leaf(team, "nom", [xml_wrapper]))
	team.children.append(Leaf(team, "age", [sql_wrapper]))
	return root