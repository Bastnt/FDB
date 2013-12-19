# -*- coding: utf-8 -*-
import mediator.splitter
from wrapper import xml_wrapper
from models import *

# This is the top
def execute(request):
	# TODO
	#if(not mediator.verifier.verify(request)):
	#	return "Invalid Syntax"

	#mediator.splitter.main(request)
	s = schema()
	mediator.splitter.main("")
	# print(s.findall("trainerName").name)


	# Tests
	#print(xml_wrapper.execute(Req("type55", "", "moves")))

if __name__ == "__main__":
	execute("")
