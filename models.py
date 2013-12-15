from tree import Node, Leaf, Attribute
from wrapper import xml_wrapper, sql_wrapper

class Req:
	def __init__(self, projection = [], selection = "", table = ""):
		self.projection = projection
		self.selection = selection
		self.table = table

class Wrapper:
	def __init__(self, name, execute_pointer):
		self.name = name
		self.execute_pointer = execute_pointer

	def execute(self, req):
		self.execute_pointer(req)

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

	sql = Wrapper("SQL", sql_wrapper.execute)
	xml = Wrapper("XML", xml_wrapper.execute)

	root = Node(None, "root")
	team = Node(root, "team")

	root.children.append(team)
	team.attributes.append(Attribute(team, "id", [sql,xml]))
	team.children.append(Leaf(team, "nom", [xml]))
	team.children.append(Leaf(team, "age", [sql]))
	return root