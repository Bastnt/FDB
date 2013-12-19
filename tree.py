# -*- coding: utf-8 -*-

# Tree classes to represent the federated schema

class Tree:
	def __init__(self, parent, name):
		self.name = name
		self.parent = parent
		if(parent):
			parent.children.append(self)

	# Find all the children with this name at any depth
	def findall(self, name):
		result = []
		self.rec_findall(name, result)
		if len(result) > 0:
			return result[0]
		else:
			return None

	# don't use this
	def rec_findall(self, name, result):
		if(self.name == name):
			result.append(self)

class Node(Tree):
	def __init__(self, parent, name):
		Tree.__init__(self, parent, name)
		self.children = []

	def find(self, name):
		for c in self.children:
			if c.name == name:
				return c

	def rec_findall(self, name, result):
		Tree.rec_findall(self, name, result)
		for c in self.children:
			c.rec_findall(name, result)


class Leaf(Tree):
	def __init__(self, parent, name, wrappers=[]):
		Tree.__init__(self, parent, name)
		self.wrappers = wrappers
		self.attributes = []

	def find(self, name):
		for a in self.attributes:
			if a.name == name:
				return a

	def rec_findall(self, name, result):
		Tree.rec_findall(self, name, result)
		for a in self.attributes:
			a.rec_findall(name, result)

class Attribute(Tree):
	def __init__(self, parent, name, wrappers=[]):
		Tree.__init__(self, parent, name)
		self.wrappers = wrappers