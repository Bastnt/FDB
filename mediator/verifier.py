# -*- coding: utf-8 -*-
# PROJET BDA SIM
# Verifier

import re

# Deals recursively with the basic elements within the clause
# Example of a basic element: $column_name2 >30
def dealWithBasicElement(parsedString,requestVariable):
	match = re.search("^[\s]*"+re.escape(requestVariable)+"(\/.+?)*[\s]*(<|>|>=|<=|=|!=|<>)[\s]*(\".+?\"|true|false|-?[0-9]+\.?[0-9]*)", parsedString)
	if match:
		return ""
	else:
		print("A basic element is not well-formed : \""+parsedString+"\". It must match the pattern : $your_var/xpath operator literal.")
		return None;

# Deals recursively with the "and" and "or" within the clause
def dealWithAndOr(parsedString,requestVariable):
	match = re.search("[\s]*\((.+?)\)[\s]+(and|or|AND|OR)[\s]+(.+)", parsedString)
	if match:
		leftAnalysis = dealWithParenthesis(match.group(1),requestVariable)
		if leftAnalysis == None:
			return None;
		return dealWithParenthesis(match.group(3),requestVariable)
	else:
		match = re.search("(.+?)[\s]+(and|or|AND|OR)[\s]+(.+)", parsedString)
		if match:
			leftAnalysis = dealWithParenthesis(match.group(1),requestVariable)
			if leftAnalysis == None:
				return None;
			return dealWithParenthesis(match.group(3),requestVariable)
		else:
			return dealWithBasicElement(parsedString,requestVariable)

# Deals recursively with the parenthesis within the clause
def dealWithParenthesis(parsedString,requestVariable):
	match = re.search("^\([\s]*(.+)[\s]*\)$", parsedString)
	if match:
		return dealWithParenthesis(match.group(1),requestVariable)
	else:
		return dealWithAndOr(parsedString,requestVariable)

# Finds the $variable of the request
def getVariable(forPart):
	parsed = re.match("^(\$.+?)[\s]+in",forPart)
	if parsed:
		return parsed.group(1);
	else: 
		print("You must precise a name for your variable in the for part : \"for $your_variable in...\"")
		return None;

# Checks whether the return part is correct or not
def dealWithReturnPart(returnPart, requestVariable):
	parsed = re.match("^[\s]*"+re.escape(requestVariable)+"[\s]*$",returnPart)
	if parsed:
		return "";
	else: 
		print("The return part must only return the $variable defined in the for part.") 
		return None;

# Checks whether the for part is correct or not
def dealWithForPart(forPart):
	# TODO : "upgrades" the ending (.+?) to be more specific and performs an semantical analysis
	parsed = re.match("^(\$.+?)[\s]+in[\s]+doc\(\".+?\"\)(.+?)$",forPart)
	if parsed:
		return parsed.group(2);
	else:
		print("The for part is not well-formed. It should follow the following pattern : for $variable in doc(\"yourdoc\")/your_xpath.") 
		return None;

# Created to format the final answer but actually quite useless
def formatAnswer(forAnalysis, wherePart):
	return (forAnalysis,wherePart)

# Performs the main job
def verify(request):
	start = re.match("^[\s]*for[\s]+(.+?)[\s]+where[\s]+(.+?)[\s]+return[\s]+(.+?)[\s]*$",request)
	if start:
		# FOR/WHERE/RETURN Case
		forPart = start.group(1)
		wherePart = start.group(2)
		returnPart = start.group(3)
		# Get the variable $something
		requestVariable = getVariable(forPart)
		if requestVariable == None:
			return None;
		else:
			whereAnalysis = dealWithParenthesis(wherePart, requestVariable)
			returnAnalysis = dealWithReturnPart(returnPart, requestVariable)
			forAnalysis = dealWithForPart(forPart)
			if forAnalysis!=None and whereAnalysis!=None and returnAnalysis!=None:
				return formatAnswer(forAnalysis, wherePart);
			else:
				print("One of the main part of the request if not well-formed, see above.")
				return None;

	start = re.match("^[\s]*for[\s]+(.+?)[\s]+return[\s]+(.+?)[\s]*$",request)
	if start:
		# FOR/RETURN Case
		forPart = start.group(1)
		returnPart = start.group(2)
		# Get the variable $something
		requestVariable = getVariable(forPart)
		if requestVariable == None:
			return None;
		else:
			returnAnalysis = dealWithReturnPart(returnPart, requestVariable)
			forAnalysis = dealWithForPart(forPart)
			if forAnalysis!=None and returnAnalysis!=None:
				return formatAnswer(forAnalysis, "");
			else:
				print("One of the main part of the request if not well-formed, see above.")
				return None;
	else:
		# BAD REQUEST Case
		print("Your request is not well-formed. It should respect either \"for...return...\" or \"for...where...return...\" syntaxes. Imbricated request are strictly forbidden." )


