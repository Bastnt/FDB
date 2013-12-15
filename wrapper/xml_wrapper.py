# -*- coding: utf-8 -*-
import xquery

db_path = "data/xml/"

def execute(request):
	# Simple example
	req = """for $element in doc("{}")//{}
			 where $element/..[@id<10]
			 return $element""".format(db_path+request.table, request.projection[0])
	print("Request: ", req)
	res = xquery.execute(req)
	return res