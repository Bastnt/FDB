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
	re.sub("(.+?)s.xml$", "\\1", request.table)
	header = "<"+request.table+"s>\n{"
	footer = "}</"+request.table+"s>"

	forPart = "for $x in doc(\""+db_path+request.table+"s.xml\")//"+request.table+"\n"
	
	if request.selection=="":
		wherePart=""
	else:
		wherePart = " where "+dealWithParenthesis(request.selection,request.table)+"\n"
	
	if len(request.projection)==0:
		returnPart = " return $x"
	else: 
		returnPart = " return \n<"+request.table+" id=\"{$x/@id}\">\n\t{"
		for i in request.projection:
			returnPart += "$x/"+i+", " 
		returnPart = returnPart[:-2]
		returnPart += "}\n</"+request.table+">\n"

	return header+forPart+wherePart+returnPart+footer;

def execute(request):
	return xquery.execute(fromPythonReqToXQuery(request))
