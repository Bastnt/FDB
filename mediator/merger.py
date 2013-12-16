# -*- coding: utf-8 -*-

# PROJET BDA SIM
# Dans ce fichier sera codé l'assembleur :
# il est responsable d'assembler les différentes données
# provenant des différents wrappers, avant de renvoyer le 
# tout au client.

# failed to install lxml on my windows machine

import xml.etree.cElementTree as ET
import sys
# sys.path.insert(0, '/usr/bin/swig/python')
# import zorba_api

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

def add_attribute(xml_path, result_path, attribute_name, attribute_value):
	xml = open(xml_path, "r")
	result = open(result_path, "w")
	
	tree = ET.parse(xml)
	root = tree.getroot()
	current_element = root
	# print(root.tag)
	search_children(current_element, attribute_name, attribute_value)

	string = ET.tostring(tree)
	string = str(string, "utf-8")
	result.write(string)
	result.close()

def search_children(current_element, attribute_name, attribute_value):
	if(current_element is not None):
		for child in current_element:
			# print(child.tag)
			child.set(attribute_name, attribute_value)
			search_children(child, attribute_name, attribute_value)

def create_binding_xml(xml1_filename, xml2_filename, template, result_path):
	temp = open(template, "r")
	result = open(result_path, "r+")

	tree = ET.parse(temp)
	root = tree.getroot()

	# je code ça en dur
	root[0].text = xml1_filename
	root[1].text = xml2_filename
	
	string = ET.tostring(tree)
	string = str(string, "utf-8")
	result.write(string)
	result.close()
	temp.close()

def main():
	print('main')
	print('******')

	print("tests")
	merge("example.xml", "merge.xsl", "result.xml")
	merge("example_b.xml", "merge.xsl", "result_b.xml")
	add_attribute("test.xml", "res_test.xml", "db", "1")

	add_attribute("file1.xml", "file1_bis.xml", "db", "1")
	add_attribute("file2.xml", "file2_bis.xml", "db", "2")
	create_binding_xml("file1_bis.xml", "file2_bis.xml", "template.xml", "template_result.xml")
	merge("template_result.xml", "merge.xsl", "result.xml")

	create_binding_xml("moves.xml", "moves2.xml", "template.xml", "moves_res.xml")
	merge("moves_res.xml", "merge.xsl", "result_moves.xml")

if __name__ == "__main__":
	main()