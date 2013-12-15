# -*- coding: utf-8 -*-

# PROJET BDA SIM
# Dans ce fichier sera codé le wrapper 1 :
# il sera l'interface entre les sous-requêtes XQuery
# provenant du diviseur et la base de donnée SQL.
# Il doit traduire les requêtes en SQL, puis traduire le
# résultat en XML avant de le renvoyer à l'assembleur.
import re

# Converts the python request into a valid SQL request
def fromPythonReqToSQL(request):
	# Selected columns from the table
	# --------------------------------------------------------
	selectedColumns = ""
	for i in request.projection:
		selectedColumns += i+", "

	return "SELECT "+selectedColumns[:-2]+" FROM "+request.table+" WHERE "+request.selection+";";

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
def fromXQueryRequestToXMLResult(request):
	sqlQuery = fromPythonReqToSQL(request)
	sqlAnswer = getSQLResult(sqlQuery)
	fromSQLAnswerToXML(sqlAnswer)

def main():	
	#request = Req(["id", "nickname", "type1"], 'type2 = "fire"', "pokemon")
	#sqlQuery = fromPythonReqToSQL(request)
	#print(sqlQuery)
	return;

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
