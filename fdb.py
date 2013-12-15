# -*- coding: utf-8 -*-
import mediator.splitter

# This is the top
def execute(request):
	# TODO
	#if(not mediator.verifier.verify(request)):
	#	return "Invalid Syntax"
	mediator.splitter.main(request)

if __name__ == "__main__":
	execute("""
		for $a in doc()//age
		where $a/../@id > 1
		return $a
		""")