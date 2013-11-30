# PROJET BDA SIM
# Dans ce fichier sera codé le schema fédéré :
# il est responsable d'importer un fichier xsd qui servira
# à vérifier la validité des requêtes XQuery provenant
# du client.

# -*- coding: utf-8 -*-

# failed to install lxml on my windows machine

import lxml.etree as ET
import sys
# sys.path.insert(0, '/usr/bin/swig/python')
# import zorba_api

def check_xq(query, global_schema):
	schema = open(global_schema, "r")
	schema.close

def merge(xml_path, xsl_path, result_path):
	example = open(xml_path, "r")
	merge = open(xsl_path, "r")
	result = open(result_path, "w")

	dom = ET.parse(example)
	xslt = ET.parse(merge)

	transform = ET.XSLT(xslt)
	newdom = transform(dom)
	string = ET.tostring(newdom)
	string = str(string, "utf-8")
	# print(string)
	result.write(string)

	example.close()
	merge.close()
	result.close()

# Mark the objects of each sub-schema with an attribute to
# easily identify the source schema of the object
def mark():
	pass

def main():
	print('main')
	print('******')
	merge("example.xml", "merge.xsl", "result.xml")
	merge("example_b.xml", "merge.xsl", "result_b.xml")

main()