# -*- coding: utf-8 -*-

# PROJET BDA SIM
# Dans ce fichier sera codé le wrapper 1 :
# il sera l'interface entre les sous-requêtes XQuery
# provenant du diviseur et la base de donnée SQL.
# Il doit traduire les requêtes en SQL, puis traduire le
# résultat en XML avant de le renvoyer à l'assembleur.
import re

# Database
db_path = "../data/sql/database.db"
# To update the database.db : go to ../data/sql/, suppress the previous database.db, open a shell and then type :
# sqlite3 database.db
# .read request_pokemon.sql 
# (and wait)
# .read request_team.sql
# (and wait)

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
def fromSQLAnswerToXML(answer, att_list):
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
	return string

def execute(request):
	global db_path
	sqlQuery = fromPythonReqToSQL(request)
	sqlAnswer = getSQLResult(sqlQuery, db_path)
	print("What to execute: ")
	print("SELECT {} FROM {} WHERE {}".format(", ".join(request.projection), request.table, request.selection))
	fromRequestToXMLResult(request)

# Testing main (can be deleted in the "release" version)
def main():	
	#print(execute(req))
	return;

if(__name__=="__main__"):
	main()
