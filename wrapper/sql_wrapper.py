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
	#TODO
	# Create HTML result in SQLite :
	#	.mode html
	#	.output output.html
	#	<request>
	#
	# Request will be output to html directly
	#
	# OUTPUT AS HTML NOT WORKING YET

	con = None

	try:
	    con = lite.connect(db_path)
	    print('Successfully connected to \"%s\"' % db_path)

	    cur = con.cursor()

	    #TODO
	    #output as HTML
	    print('executing \"%s\"' % sqlQuery)
	    cur.execute(sqlQuery)
	    
	    data = cur.fetchall()
	    
	    print("RESULT: ", data)            
	    
	except lite.Error as e:
	    
	    print("Error %s" % e.args[0])
	    sys.exit(1)
	    
	finally:
	    
	    if con:
	        con.close()

	return;

# Transforms the SQL answer into a XML string to be sent to the mediator
def fromSQLAnswerToXML(answer_path, att_list):
	#TODO
	htmlAnswer = open(answer_path, 'r')
	tree = ET.parse(htmlAnswer)
	xmlAnswer = '<objects>' + '\n'

	root = tree.getroot()
	children = list(root)
	print('root: ', root.tag)
	
	# Ok, les \n c'est trop moche, mais pas le temps hein !

	for child in children:
		xmlAnswer += '<pokemon>' + '\n'
		values = list(child)
		for i in range(0, len(att_list)):
			print('att, val : ', att_list[i], values[i].text)
			xmlAnswer += '<' + att_list[i] + '>' + '\n'
			xmlAnswer += values[i].text
			xmlAnswer += '</' + att_list[i] + '>' + '\n'
		xmlAnswer += '</pokemon>' + '\n'
	xmlAnswer += '</objects>'

	print(xmlAnswer)
	return xmlAnswer;

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

if(__name__=="__main__"):
	main()
