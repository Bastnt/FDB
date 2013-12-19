##
## Verifier les xQuery reçu
##
##
import re

patternDoc  = re.compile(r'schema_federe.xml')
patternVar1 = re.compile(r"for (\w+) in doc")
patternVar2 = re.compile(r'where (\w+)')
patternVar3 = re.compile(r'return (\w+)')


def verifier(xRequest):
		doc = patternDoc.findall(xRequest)
		if len(doc) == 0:
			print "la base de donnees n'existe pas"
			return False
	
		var  = patternVar1.findall(xRequest)
		var2 = patternVar2.findall(xRequest)
		var3 = patternVar3.findall(xRequest)
		
		if len(var) == 0 or len(var2)==0 or len(var3)==0:
			print "Le syntaxe n'est pas correct"
			return False
		elif not(var[0]==var2[0]==var3[0]):
			print "Le syntaxe n'est pas correct"
			return False
		else:
	#		print var[0], var2[0], var3[0]
			return True
	