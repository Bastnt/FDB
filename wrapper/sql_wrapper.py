# -*- coding: utf8 -*-

# PROJET BDA SIM
# Dans ce fichier sera codé le wrapper 1 :
# il sera l'interface entre les sous-requêtes XQuery
# provenant du diviseur et la base de donnée SQL.
# Il doit traduire les requêtes en SQL, puis traduire le
# résultat en XML avant de le renvoyer à l'assembleur.
import re
import xml.etree.cElementTree as ET
import sys
import sqlite3 as lite

# Database
db_path = "data/sql/database.db"
# To update the database.db : go to ../data/sql/, suppress the previous database.db, open a shell and then type :
# sqlite3 database.db
# .read request_pokemon.sql 
# (and wait)
# .read request_team.sql
# (and wait)

# Converts the python Req into a valid SQL request
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
	    cursor.execute(sqlQuery)
	    
	    # Get all results
		# --------------------------------------------------------
	    data = cursor.fetchall()
	    
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
def fromSQLAnswerToXML(answer, request):
	# Create XML result tree
	# --------------------------------------------------------
	if(request.table == "pokemon"):
		root = ET.Element("pokemons")
	else:
		root = ET.Element("teams")

	for tupleAnswer in answer:
		child = ET.SubElement(root, request.table)
		for i in range(0, len(request.projection)):
			att = ET.SubElement(child, request.projection[i])
			att.text = str(tupleAnswer[i])

	# Write XML tree to output file
	# --------------------------------------------------------
	string = ET.tostring(root)
	string = str(string, "utf-8")
	return string

def execute(request):
	sqlQuery = fromPythonReqToSQL(request)
	sqlAnswer = getSQLResult(sqlQuery, db_path)
	return fromSQLAnswerToXML(sqlAnswer, request)

# --------------------------------------------------------
# DELETE CONTENT BELOW FOR RELEASE
# --------------------------------------------------------
# class Req:
# 	def __init__(self, projection = [], selection = "", table = ""):
# 		self.projection = projection
# 		self.selection = selection
# 		self.table = table

# def main():	
# 	#print(execute(req))
# 	requete = Req(["trainerName", "victoryCounter"],"victoryCounter > 90","team")
# 	print(execute(requete))
# 	return;

# if(__name__=="__main__"):
# 	main()
