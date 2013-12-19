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
	#s = schema()
	#for c in s.findall("pokemon").children:
	#	print(c.name)

	ex = """for $var in doc("schema_federe.xml")//trainerName[. <> 'p']/../@id return $var"""
	simplified_request = verifier.verify(ex)
	if(simplified_request == None):
		return None

	splitter.main(simplified_request)



	# Tests
	#print(xml_wrapper.execute(Req("type55", "", "moves")))

if __name__ == "__main__":
	execute("")
