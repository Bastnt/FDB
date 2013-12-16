from tree import Node, Attribute, Leaf
from wrapper import xml_wrapper, sql_wrapper

class Req:
	def __init__(self, projection = [], selection = "", table = ""):
		self.projection = projection
		self.selection = selection
		self.table = table

class Database:
	def __init__(self, name, table, wrapper_execute_pointer):
		self.name = name
		self.table = table
		self.executer = wrapper_execute_pointer

	def execute(self, req):
		req.table = self.table
		self.executer(req)

def schema():
	# dummy Schema

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

	sql_pokemon = Database("SQL", "pokemon", sql_wrapper.execute)
	xml_moves = Database("XML", "moves.xml", xml_wrapper.execute)

	root = Node(None, "root")
	team = Node(root, "team")

	root.children.append(team)
	team.children.append(Attribute(team, "@id", [sql_pokemon,xml_moves]))
	team.children.append(Leaf(team, "nom", [xml_moves]))
	team.children.append(Leaf(team, "age", [sql_pokemon]))
	return root