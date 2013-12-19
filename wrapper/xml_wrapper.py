# -*- coding: utf-8 -*-

import re
import xquery

# Database
db_path = "data/xml/"

xMLTables = {
	"move" : ["@id", "name", "type", "spePhySta", "power", "accuracy", "pp", "description"],
	"pokemon" : ["@id", "type1", "type2"],
	"team" : ["@id"]
}

# Deals recursively with the basic elements within the clause
# Example of a basic element: column_name2 >30
def dealWithBasicElement(parsedString,table):
	# 1-children
	for i in xMLTables[table]:
		match = re.search("("+i+")", parsedString)
		if match:
			return re.sub("("+i+")", "$x//\\1", parsedString)
	# n-children
	match = re.search("[\s]+(.+?)\/", parsedString)
	if match:
		return re.sub("("+i+")", "$x//\1", parsedString)

# Deals recursively with the "and" and "or" within the clause
def dealWithAndOr(parsedString,table):
	match = re.search("(.+?)[\s]+(and|or|AND|OR)[\s]+(.+)", parsedString)
	if match:
		return dealWithParenthesis(match.group(1),table)+" "+match.group(2)+" "+dealWithParenthesis(match.group(3),table)
	else:
		return dealWithBasicElement(parsedString,table)

# Deals recursively with the parenthesis within the clause
def dealWithParenthesis(parsedString,table):
	match = re.search("\([\s]*(.+)[\s]*\)", parsedString)
	if match:
		return "("+dealWithParenthesis(match.group(1),table)+")"
	else:
		return dealWithAndOr(parsedString,table)

# Converts the python Req into a valid XQuery request
def fromPythonReqToXQuery(request):
	header = "<"+request.table+">\n{"
	footer = "}</"+request.table+">"

	forPart = "for $x in doc(\""+db_path+request.table+".xml\")//"+request.projection+"\n"
	
	if request.selection=="":
		wherePart=""
	else:
		wherePart = " where "+dealWithParenthesis(request.selection,request.table)+"\n"

	returnPart = " return $x"

	print(header+forPart+wherePart+returnPart+footer)
	return header+forPart+wherePart+returnPart+footer;

def execute(request):
	return xquery.execute(fromPythonReqToXQuery(request))
