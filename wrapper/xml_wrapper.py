# -*- coding: utf-8 -*-

import re
import xquery

# Database
db_path = "data/xml/"

xMLTables = {
	"moves" : ["@id", "name", "type", "spePhySta", "power", "accuracy", "pp", "description"],
	"pokemons" : ["@id", "type1", "type2"],
	"teams" : ["@id"]
}

# Deals recursively with the basic elements within the clause
# Example of a basic element: column_name2 >30
def dealWithBasicElement(parsedString,table):
	# 1-children
	for i in xMLTables[table]:
		match = re.search("("+i+")", parsedString)
		if match:
			return re.sub("("+i+")", "$x/\\1", parsedString)
	# n-children
	match = re.search("[\s]+(.+?)\/", parsedString)
	if match:
		return re.sub("("+i+")", "$x//\1", parsedString)
	else:
		print("ERROR, should have been filtered before by the Verifier")
		return None

# Deals recursively with the "and" and "or" within the clause
def dealWithAndOr(parsedString,table):
	match = re.search("[\s]*\((.+?)\)[\s]+(and|or|AND|OR)[\s]+(.+)", parsedString)
	if match:
		return dealWithParenthesis(match.group(1),table)+" "+match.group(2)+" "+dealWithParenthesis(match.group(3),table)
	else:
		match = re.search("(.+?)[\s]+(and|or|AND|OR)[\s]+(.+)", parsedString)
		if match:
			return dealWithParenthesis(match.group(1),table)+" "+match.group(2)+" "+dealWithParenthesis(match.group(3),table)
		else:
			return dealWithBasicElement(parsedString,table)

# Deals recursively with the parenthesis within the clause
def dealWithParenthesis(parsedString,table):
	match = re.search("^\([\s]*(.+)[\s]*\)$", parsedString)
	if match:
		return "("+dealWithParenthesis(match.group(1),table)+")"
	else:
		return dealWithAndOr(parsedString,table)

# Converts the python Req into a valid XQuery request
def fromPythonReqToXQuery(request):
	header = "<"+request.table+">\n{"
	footer = "}</"+request.table+">"

	forPart = "for $x in doc(\""+db_path+request.table+".xml\")//"+request.table[:-1]+"\n"
	
	if request.selection=="":
		wherePart=""
	else:
		wherePart = " where "+dealWithParenthesis(request.selection,request.table)+"\n"
	
	if(request.projection!= "@id"):
		returnPart = " return <"+request.table[:-1]+" id=\"{$x/@id}\">\n\t{$x/"+request.projection+"}\n</"+request.table[:-1]+">\n"
	else:
		returnPart = " return <"+request.table[:-1]+" id=\"{$x/@id}\"/>\n"
	print(header+forPart+wherePart+returnPart+footer)
	return header+forPart+wherePart+returnPart+footer;

def execute(request):
	return xquery.execute(fromPythonReqToXQuery(request))
