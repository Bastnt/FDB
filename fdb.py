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


	# Tests
	#print(xml_wrapper.execute(Req(['name'], "", "moves.xml")))

if __name__ == "__main__":
	request = Req(["type"],"power >= 40","move")
	print(xml_wrapper.execute(request))
