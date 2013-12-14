# -*- coding: utf-8 -*-
import xquery

request = """for $t in doc("DB2.xml")//team
return <team1>{$t//nickname}</team1>"""

xquery.execute(request)