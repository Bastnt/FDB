# -*- coding: utf-8 -*-

# PROJET BDA SIM
# Dans ce fichier sera codé l'assembleur :
# il est responsable d'assembler les différentes données
# provenant des différents wrappers, avant de renvoyer le 
# tout au client.

# failed to install lxml on my windows machine

from xml.etree import ElementTree as et
import sys

# sys.path.insert(0, '/usr/bin/swig/python')
# import zorba_api

class XMLCombiner(object):
    def __init__(self, filenames):
        assert len(filenames) > 0, 'No filenames!'
        # save all the roots, in order, to be processed later
        self.roots = [et.parse(f).getroot() for f in filenames]

    def combine(self):
        for r in self.roots[1:]:
            # combine each element with the first one, and update that
            self.combine_element(self.roots[0], r)
        # return the string representation
        return et.tostring(self.roots[0])

    def combine_element(self, one, other):
        """
        This function recursively updates either the text or the children
        of an element if another element is found in `one`, or adds it
        from `other` if not found.
        """
        # Create a mapping from tag name to element, as that's what we are fltering with
        mapping = {el.tag: el for el in one}
        for el in other:
            if len(el) == 0:
                # Not nested
                try:
                    # Update the text
                    mapping[el.tag].text = el.text
                except KeyError:
                    # An element with this name is not in the mapping
                    mapping[el.tag] = el
                    # Add it
                    one.append(el)
            else:
                try:
                    # Recursively process the element, and update it in the same way
                    self.combine_element(mapping[el.tag], el)
                except KeyError:
                    # Not in the mapping
                    mapping[el.tag] = el
                    # Just add it
                    one.append(el)

"""
if __name__ == '__main__':
    r = XMLCombiner(('sample1.xml', 'sample2.xml')).combine()
    print '-'*20
    print r
"""

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

	r = XMLCombiner(('fichiers test/file1.xml', 'fichiers test/file2.xml')).combine()
	print(r)


	"""
	merge("example.xml", "merge.xsl", "result.xml")
	merge("example_b.xml", "merge.xsl", "result_b.xml")
	add_attribute("test.xml", "res_test.xml", "db", "1")

	add_attribute("file1.xml", "file1_bis.xml", "db", "1")
	add_attribute("file2.xml", "file2_bis.xml", "db", "2")
	create_binding_xml("file1_bis.xml", "file2_bis.xml", "template.xml", "template_result.xml")
	merge("template_result.xml", "merge.xsl", "result.xml")

	create_binding_xml("moves.xml", "moves2.xml", "template.xml", "moves_res.xml")
	merge("moves_res.xml", "merge.xsl", "result_moves.xml")
	"""
if __name__ == "__main__":
	main()