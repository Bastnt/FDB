# -*- coding: utf-8 -*-
import re
from models import *
from decision_algorithm import *
import xml.etree.cElementTree as ET

# PROJET BDA SIM
# Dans ce fichier sera codé le diviseur :
# il est responsable de diviser une requête XQuery valable
# en différentes sous-requêtes, avant d'interroger les bases
# via les wrappers

header = """<?xml version="1.0" encoding="UTF-8"?>"""

def main(simplified_request):
	parse_cursor = schema()

	# Parsing du XQ

	# We catch the xpath part of the for clause
	# We catch the condition part of the where clause
	for_content, where_content = simplified_request

	# We append the where_content to the xpath of the for_content in order
	# to just have a one line xpath query to resolve
	if where_content != "":
		for_content += "[."+where_content+"]"

	# get the last Node of the path, the one to return
	returnNode, conditionList = parse_xpath(parse_cursor, for_content)
	if returnNode == None:
		return empty_result()

		# Here are the results of the complete parsing
	print("\nreturnObject: "+returnNode.name)
	print("conditions: ")
	for c in conditionList:
		if c != None:
			print("Condition("+c.node.name+c.condition+")")


	# We now call the decision algorithm
	print("\nJoins: ")
	print(returnNode.name)
	for c in conditionList:
		clusters, join_attribute = join_decision(c.node, returnNode)
		cond = c.node.name + c.condition
		for i in range(0,len(clusters)-1):
			print(clusters[i].origin)
			if clusters[i].origin == "sql":
				res = clusters[i].executer(Req(join_attribute[i], cond, clusters[i].table))
				tree = ET.fromstring(res)
				res = []
				for c in tree.getchildren():
					res.append("@"+join_attribute[i]+" = \""+c.attrib[join_attribute[i]]+"\"")
				cond=" or ".join(res)

			elif clusters[i].origin == "xml":
				res = clusters[i].executer(Req(join_attribute[i], cond, clusters[i].table))
				tree = ET.fromstring(res)
				res = []
				for c in tree.getchildren():
					res.append("@"+join_attribute[i]+" = \""+c.attrib[join_attribute[i]]+"\"")
				cond=" or ".join(res)
				print(cond)

		return clusters[-1].executer(Req(returnNode.name, cond, clusters[-1].table))



def parse_xpath(cursor, expression):
	# The conditions to apply
	conditions = []

	# We put all the attributes and the [conditions] in a list representing a full path
	full_path = re.findall("//?[@\w\.]+|\[.+?\]", expression)

	print("Analyse: ", full_path)

	for a in full_path:
		token = re.search("(//?|\[)(.+?)\]?$", a)
		try:
			type = token.group(1)
			name = token.group(2)
		except:
			print("Error in splitting a xpath token in: "+a)
			exit()

		if type == "[":
			c = re.search("^([/?\w@\.]+)(.+)$", name)
			n, _ = parse_xpath(cursor, c.group(1))
			conditions.append(Condition(n, c.group(2)))


		if name == "..":
			cursor = cursor.parent
			continue
		elif name == ".":
			continue

		if type == "//":
			node = cursor.findall(name)
		elif type == "/":
			node = cursor.find(name)

		if not node:
			return None, []
		cursor = node

	if(isinstance(cursor, Node)):
		return None, []
	else:
		return cursor, conditions

def empty_result():
	return header+"<results />"

def parse(mask, string):
	found = re.search(mask, string)
	assert found != None, ("Error while parsing:\n"+string)
	return found.group(1)