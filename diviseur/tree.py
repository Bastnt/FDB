# -*- coding: utf-8 -*-

# Tree classes to represent the federated schema

class Tree:
	def __init__(self, parent, name):
		self.name = name
		self.parent = parent

	# Find all the the tags with this name
	def find_all(self, name):
		result = []
		self.rec_find_all(name, result)
		return result

	# don't use this
	def rec_find_all(self, name, result):
		if(self.name == name):
			result.append(self)

	# Find all the the attributes with this name
	def find_all_attributes(self, name):
		result = []
		self.rec_find_all_attributes(name, result)
		return result

	# don't use this
	def rec_find_all_attributes(self, name, result):
		for a in self.attributes:
			if(a.name == name):
				result.append(a)

class Node(Tree):
	def __init__(self, parent, name):
		Tree.__init__(self, parent, name)
		self.children = []
		self.attributes = []

	def rec_find_all(self, name, result):
		Tree.rec_find_all(self, name, result)
		for c in self.children:
			c.rec_find_all(name, result)

	def rec_find_all_attributes(self, name, result):
		Tree.rec_find_all_attributes(self, name, result)
		for c in self.children:
			c.rec_find_all_attributes(name, result)

class Leaf(Tree):
	def __init__(self, parent, name, wrappers=[]):
		Tree.__init__(self, parent, name)
		self.wrappers = wrappers
		self.attributes = []

class Attribute(Tree):
	def __init__(self, parent, name, wrappers=[]):
		Tree.__init__(self, parent, name)
		self.wrappers = wrappers