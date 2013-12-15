# -*- coding: utf-8 -*-
import subprocess
import re

xquery_processor = "zorba/bin/zorba.exe"

def execute(req):
	proc = subprocess.Popen([xquery_processor, "-q", req], stdout=subprocess.PIPE)
	out, err = proc.communicate()
	return re.sub("\\\.", "", str(out))