import xquery

print(xquery.execute("for $a in doc('data/xml/moves.xml')//power[. > 10][./../@id < 10] return $a"))