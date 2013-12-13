# -*- coding: utf-8 -*-
import schema
import re

# PROJET BDA SIM
# Dans ce fichier sera codé le diviseur :
# il est responsable de diviser une requête XQuery valable
# en différentes sous-requêtes, avant d'interroger les bases
# via les wrappers


my_schema = schema.schema()

client_example_request = """
	for $a in doc()//age
	where $a/../@id > 1
	return $a
"""

print("The request to split: ")
print(client_example_request)

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
request = schema.Req(["age"], "id > 1")
ages[0].wrappers[0].execute(request)