# -*- coding: utf-8 -*-

# PROJET BDA SIM
# Dans ce fichier sera codé le wrapper 1 :
# il sera l'interface entre les sous-requêtes XQuery
# provenant du diviseur et la base de donnée SQL.
# Il doit traduire les requêtes en SQL, puis traduire le
# résultat en XML avant de le renvoyer à l'assembleur.
import re

"""
for $x in sql/table_name
where d and a or b and c or k and (y or j)
return $x/column_name3
"""

# Globals
table_name = 0
tuple_name = 0

# Lexical analysis of the xQuery request
def lexicalAnalysis(request):
	#TODO : be more specific
	match = re.search("for[\s]+(.+)[\s]+where[\s]+(.+)[\s]+return[\s]+(.+)", request)
	if match:
	   print("SELECT: ", match.group(3))
	   print("FROM: ", match.group(1))
	   print("WHERE: ", match.group(2))
	   return match
	else:
	   print("No match!!")
	return;

# Syntaxical analysis of the three parts of the xQuery request
def syntaxicalAnalysis(subdividedQuery):
	#TODO
	return;

# Semantical analysis of the three parts of the xQuery request
def semanticalAnalysis(subdividedQuery):
	#TODO
	return;

# Analysis the xQuery request from the mediator, checks its correctness
def analyse(xqueryRequest):
	match = lexicalAnalysis(xqueryRequest)
	syntaxicalAnalysis(match)
	semanticalAnalysis(match)
	return match

# Deals recursively with the basic elements within the clause
# !! Use of globals variables table_name and tuple_name that must have been initialized !!
# !! tuple_name starts with a "$", escaping required !!
# Example of a basic element: $x/column_name2 >30
def dealWithBasicElement(parsedString):
	# TODO

# Deals recursively with the "and" and "or" within the clause
def dealWithAndOr(parsedString):
	match = re.search("(.+)[\s]+([and|or|AND|OR])[\s]+(.+)", parsedString)
	if match:
		return dealWithParenthesis(match.group(1))+" "+match.group(2).upper()+" "+dealWithParenthesis(match.group(3))
	else:
		return dealWithBasicElement(parsedString)

# Deals recursively with the parenthesis within the clause
def dealWithParenthesis(parsedString):
	match = re.search("\([\s]*(.+)[\s]*\)", parsedString)
	if match:
		return "("+dealWithParenthesis(match.group(1))+")"
	else:
		return dealWithAndOr(parsedString)

# Converts the three parts of a validated xQuery request into a valid SQL request
def fromXQueryPartsToSQL(selectPart, fromPart, wherePart):
	global table_name
	global tuple_name
	# Table name and tuple name
	# --------------------------------------------------------
	parsedFromPart = re.search("(.+)[\s]+in[\s]+sql/(.+)", fromPart)
	table_name = parsedFromPart.group(2)
	tuple_name = parsedFromPart.group(1)

	# Selected column from the table
	# --------------------------------------------------------
	parsedSelectPart = re.search("^\\"+tuple_name+"/(.+)$", selectPart) # Be careful here because tuple_name starts with a "$"" which must be escaped with the appropriate "\"
	if parsedSelectPart:
		selectedColumn = parsedSelectPart.group(1)
	else:
		selectedColumn = "*"

	# "Where" part of the query
	# --------------------------------------------------------
	whereClauses = dealWithParenthesis(wherePart)

	return "SELECT "+selectedColumn+" FROM "+table_name" WHERE "+whereClauses+";";

# Performs the SQL request on the database
def getSQLResult(sqlQuery, db_path):
	connection = None

	try:
		# Connect to the database.db
		# --------------------------------------------------------
	    connection = lite.connect(db_path)
	    print('Successfully connected to \"%s\"' % db_path)
	    cursor = connection.cursor()

		# Execute SQL query
		# --------------------------------------------------------
	    print('executing \"%s\"' % sqlQuery)
	    cursor.execute(sqlQuery)
	    
	    # Get all results
		# --------------------------------------------------------
	    data = cursor.fetchall()
	    print("RESULT: ", data)  
	    
	except lite.Error as e:
	    
	    print("Error %s" % e.args[0])
	    sys.exit(1)
	    
	finally:
	    # Close database connection
		# --------------------------------------------------------
	    if connection:
	        connection.close()

	return data;

# Transforms the SQL answer into a XML string to be sent to the mediator
def fromSQLAnswerToXML(answer, att_list, output_path):
	# Open XML output file
	# --------------------------------------------------------	
	result = open(output_path, "w")

	# Create XML result tree
	# --------------------------------------------------------
	root = ET.Element("pokemons")
	for pokemon in answer:
		pokemon = ET.SubElement(root, "pokemon")
		for element in answer:
			for i in range(0, len(att_list)):
				att = ET.SubElement(pokemon, att_list[i])
				att.text = str(element[i])

	# Write XML tree to output file
	# --------------------------------------------------------
	string = ET.tostring(root)
	string = str(string, "utf-8")
	result.write(string)

	# Close XML output file
	# --------------------------------------------------------
	result.close()

# Performs the main job
def fromXQueryRequestToXMLResult(xqueryRequest):
	match = analysis(xqueryRequest)
	sqlQuery = fromXQueryPartsToSQL(match.group(3), match.group(1), match.group(2))
	sqlAnswer = getSQLResult(sqlQuery)
	fromSQLAnswerToXML(sqlAnswer)

def main():	
	match = lexicalAnalysis("""for $x in sql/table_name
	where $x/column_name2 >30 and column_name1 == "blabla"
	return $x""")

	sqlQuery = fromXQueryPartsToSQL(match.group(3), match.group(1), match.group(2))

	print(sqlQuery)

	print("-----------tests getSQLResult and fromSQLAnswerToXML-----------")

	#answer_path = '/home/richard/Downloads/test.html'
	#list = ['id', 'name']
	#fromSQLAnswerToXML(answer_path, list)

	#db_path = 'SQL DB/temp.db'
	#sqlQuery = 'SELECT * FROM pokemon WHERE id=1'
	#answer = getSQLResult(sqlQuery, db_path)
	#att_list = ['id', 'name']
	#output_path = 'result.xml'

	#fromSQLAnswerToXML(answer, att_list, output_path)

if(__name__=="__main__"):
	main()
