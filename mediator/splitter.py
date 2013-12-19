# -*- coding: utf-8 -*-
import re
from models import *

# PROJET BDA SIM
# Dans ce fichier sera codé le diviseur :
# il est responsable de diviser une requête XQuery valable
# en différentes sous-requêtes, avant d'interroger les bases
# via les wrappers

def main(request):
	my_schema = schema()

	# Parsing du XQ
	ex = """for $var in doc("")//pokemon/name//nickname[../@id>10]
			where $var/../@id = 12
			return $var
	"""

	attribute_mask = re.compile("for.+?(//?[@A-Za-z0-9]+(\[.+?\])?)+")

	ans = attribute_mask.search(ex)

	print(ans.group(1))
	print(ans.group(2))
	print(ans.group(3))




	print("The request to split: ")
	print(request)

	# === Example non automated: ===
	ages = my_schema.find_all("age")
	print("We can find 'age' in the following databases: ")
	for age in ages:
		for wrapper in age.wrappers:
			print("-", wrapper.name)

	ids = my_schema.find_all_attributes("id")
	print("We can find '@id' in the following databases: ")
	for id in ids:
		for wrapper in id.wrappers:
			print("-", wrapper.name)

	# They are on the same database, so the request will be:
	req = Req(["age"], "id > 1", "pokemon.db")
	ages[0].wrappers[0].execute(req)

if __name__ == "__main__":
	main()