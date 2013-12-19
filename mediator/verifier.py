# -*- coding: utf-8 -*-
# PROJET BDA SIM
# Verifier

import re

"""
for_content = parse("for.+?\)(.+?)(\n|\s+(where|return))", reqsimplified_request)
where_content = parse("where\s+\$\w+(.+?)(\n|\s+(where|return))", request)
"""

def verify(request):
	return "//trainerName[. <> 'p']/../@id", ""