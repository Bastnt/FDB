import re

# -*- coding: utf-8 -*-

# PROJET BDA SIM
# Dans ce fichier sera codé le wrapper 1 :
# il sera l'interface entre les sous-requêtes XQuery
# provenant du diviseur et la base de donnée SQL.
# Il doit traduire les requêtes en SQL, puis traduire le
# résultat en XML avant de le renvoyer à l'assembleur.
"""
for $x in sql/table_name
where $x/column_name2 >30 and $x/column_name1 == "blabla"
return $x/column_name3
"""

# Lexical analysis of the xQuery request
def lexicalAnalysis( xqueryRequest ):
	#TODO : be more specific
	match = re.search("for (.+)[\s]+where (.+)[\s]+return (.+)", request)
	if match:
	   print("SELECT: ", match.group(3))
	   print("FROM: ", match.group(1))
	   print("WHERE: ", match.group(2))
	   return match
	else:
	   print("No match!!")
	return;

# Syntaxical analysis of the three parts of the xQuery request
def syntaxicalAnalysis( subdividedQuery ):

# Semantical analysis of the three parts of the xQuery request
def semanticalAnalysis( subdividedQuery ):

# Analysis the xQuery request from the mediator, checks its correctness
def analyse( xqueryRequest):
	match = lexicalAnalysis(xqueryRequest)
	syntaxicalAnalysis(match)
	semanticalAnalysis(match)
	return match

# Converts the three parts of a xQuery request into a valid SQL request
def fromXQueryPartsToSQL(selectPart, fromPart, wherePart):

# Performs the SQL request on the database
def getSQLResult(sqlQuery):

# Transforms the SQL answer into a XML string to be sent to the mediator
def fromSQLAnswerToXML(sqlAnswer):



# Performs the main job
def fromXQueryRequestToXMLResult(xqueryRequest):
	match = analysis(xqueryRequest)
	sqlQuery = fromXQueryPartsToSQL(match.group(3), )
	sqlAnswer = getSQLResult(sqlQuery)
	fromSQLAnswerToXML(sqlAnswer)
	


def main():	
	lexicalAnalysis("""for $x in sql/table_name
	where $x/column_name2 >30
	return $x/column_name3""")

if(__name__=="__main__"):
	main()
