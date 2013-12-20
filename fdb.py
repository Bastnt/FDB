# -*- coding: utf-8 -*-
from mediator import splitter, verifier
from wrapper import xml_wrapper
from models import *

# This is the top
def execute(request):
	# TODO
	#if(not mediator.verifier.verify(request)):
	#	return "Invalid Syntax"

	#mediator.splitter.main(request)
	# s = schema()
	# victory = s.findall("victoryCounter")
	# defeat = s.findall("defeatCounter")
	# print(find_join_path.find_join_path(s, victory, defeat))

	#for c in s.findall("pokemon").children:
	#	print(c.name)

	ex = """for $type1 in doc("schema_federe.xml")//team[/victoryCounter > 90]//type1 return $type1"""
	simplified_request = verifier.verify(ex)

	result = splitter.main(simplified_request)

	f=open("RESULT1.XML", "w")
	f.write(result)
	f.close()

	ex = """for $trainerName in doc("schema_federe.xml")//team[/defeatCounter > 75]/trainerName return $trainerName"""
	simplified_request = verifier.verify(ex)

	result = splitter.main(simplified_request).decode("utf8")

	f=open("RESULT2.XML", "w")
	f.write(result)
	f.close()
	# if(simplified_request == None):
	# 	return None

	

	

	print("SUCCESS")

	# Tests
	#print(xml_wrapper.execute(Req("type55", "", "moves")))

if __name__ == "__main__":
	execute("")
