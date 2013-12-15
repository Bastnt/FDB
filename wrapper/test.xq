for $t in doc("DB2.xml")//team[@id=1]
return <team1>{$t//nickname}</team1>