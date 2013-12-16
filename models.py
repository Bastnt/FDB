from tree import Node, Attribute, Leaf
from wrapper import xml_wrapper, sql_wrapper

class Req:
	def __init__(self, projection = [], selection = "", table = ""):
		self.projection = projection
		self.selection = selection
		self.table = table

class Cluster:
	def __init__(self, origin, table, wrapper_execute_pointer):
		self.origin = origin # Whether "sql" or "xml"
		self.table = table
		self.executer = wrapper_execute_pointer

	def execute(self, req):
		req.table = self.table
		self.executer(req)

def schema():
	# === XML example verified by this schema: ===
	# <Node:pokemonData>
	# 	<Node:teams Attribute:id="1">
	# 		<Node:team Attribute:id="1" >
	#			<Leaf:trainerName>Billy</Leaf:trainerName>
	#		</Node:team>
	# 	</Node:teams>
	# </Node:pokemonData>

	sql_pokemon = Cluster("sql", "pokemon", sql_wrapper.execute)
	sql_team = Cluster("sql", "team", sql_wrapper.execute)
	xml_moves = Cluster("xml", "moves", xml_wrapper.execute)
	xml_team = Cluster("xml", "teams", xml_wrapper.execute)
	xml_pokemon = Cluster("xml", "pokemons", xml_wrapper.execute)

	root = Node(None, "pokemonData")
	teams = Node(root, "teams")
	moves = Node(root, "moves")
	pokedex = Node(root, "pokedex")

	team = Node(team, "team")
	Leaf(team, "trainerName", [sql_team])
	Leaf(team, "victoryCounter", [sql_team])
	Leaf(team, "defeatCounter", [sql_team])
	Attribute(team, "@id", [sql_pokemon,xml_moves])

	pokemon = Node(team, "pokemon")
	Leaf(pokemon, "nickname", [xml_team])
	Leaf(pokemon, "name", [sql_pokemon])
	Leaf(pokemon, "height", [sql_pokemon])
	Leaf(pokemon, "weight", [sql_pokemon])
	Leaf(pokemon, "type1", [xml_pokemon])
	Leaf(pokemon, "type2", [xml_pokemon])
	Leaf(pokemon, "base_experience", [sql_pokemon])
	Attribute(pokemon, "@id", [sql_pokemon,xml_team,xml_pokemon])

	movePokemon = Node(pokemon, "move")
	Leaf(movePokemon, "spePhySta", [xml_moves])
	Leaf(movePokemon, "power", [xml_moves])
	Leaf(movePokemon, "accuracy", [xml_moves])
	Leaf(movePokemon, "pp", [xml_moves])
	Leaf(movePokemon, "description", [xml_moves])
	Attribute(movePokemon, "@id", [xml_team, xml_moves])

	move = Node(pokemon, "move")
	Leaf(move, "spePhySta", [xml_team])
	Leaf(move, "power", [xml_moves])
	Leaf(move, "accuracy", [xml_moves])
	Leaf(move, "pp", [xml_moves])
	Leaf(move, "description", [xml_moves])
	Attribute(move, "@id", [xml_moves])

	pokemonPokedex = Node(team, "pokemon")
	Leaf(pokemonPokedex, "name", [sql_pokemon])
	Leaf(pokemonPokedex, "height", [sql_pokemon])
	Leaf(pokemonPokedex, "weight", [sql_pokemon])
	Leaf(pokemon, "type1", [xml_pokemon])
	Leaf(pokemon, "type2", [xml_pokemon])
	Leaf(pokemonPokedex, "base_experience", [sql_pokemon])
	Attribute(pokemonPokedex, "@id", [sql_pokemon,xml_pokemon])
	
	return root