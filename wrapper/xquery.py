# -*- coding: utf-8 -*-
import subprocess

xquery_processor = "zorba/bin/zorba.exe"


def execute(req):
	proc = subprocess.Popen([xquery_processor, "-q", req], stdout=subprocess.PIPE)
	out, err = proc.communicate()
	print(out)