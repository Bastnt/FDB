import random

f = open('request_team.sql','w')
toWrite = """CREATE TABLE team (
  id INTEGER NOT NULL,
  trainerName VARCHAR(50) NOT NULL,
  victoryCounter INTEGER NOT NULL,
  defeatCounter INTEGER NOT NULL
);\n\n"""

name = ["vrignaud","thoumelin","thoux","sy","sieurin","seillan","rossetti","robin","robert","peron","noel","mesdouri","mbasso","mathieu","masson","mammeri","malkas","madiot","lorilleux","li","lhonore","lepennec","lemercier","leger","lefeuvre","le cahain","laperdrix","langlais","lagrange","hinsinger","hammouda","guirinec","guilpain","guegant","guionnet","granger","gilles","georget","gardan","ferrand","favre","fauvet","fabry","el marzgioui","djedai","desiles","couka","chausse","charrier","carteron","brunelat","boutet","berland","berrard","berge","bergaoui","bailleul","artur","amhachi","aanor","aaron","abbon","abby","abdel","abdon","abel","abelard","abelia","abella","abigael","abondance","abraham","acace","achille","acme","ada","adalard","adalbert","adalric","adalsinde","adam","adama","adelaide","adelais","adelard","adele","adelice","adelie","adelin","adelind","adeline","adelphe","adelphine","adeltrude","ademar","adenora","adine","adolphe","adon","adonis","adore"]
res = []
for i in range(0,100):
	res.append("""INSERT INTO team VALUES({}, "{}", {}, {});\n""".format(i, name[i], random.randint(0,99), random.randint(0,99)))
f.write(toWrite)
f.write("".join(res))
f.close()