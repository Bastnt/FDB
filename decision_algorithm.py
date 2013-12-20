# -*- coding: utf-8 -*-
#!/usr/local/bin/python

# from tree import Node, Tree, Leaf, Attribute
from models import *

# ================ STUB ====================

def join_decision(tree1, tree2):
	if tree1.name == "victoryCounter" and tree2.name == "type1":
		return [sql_team, xml_team, xml_pokemon], ["id", "id"]
	if tree1.name == "defeatCounter" and tree2.name == "trainerName":
		return [sql_team], []