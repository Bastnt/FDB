import random

f = open('request_team.sql','w')
f.write("""CREATE TABLE team (
  id INTEGER NOT NULL,
  trainerName VARCHAR(50) NOT NULL,
  victoryCounter INTEGER NOT NULL,
  defeatCounter INTEGER NOT NULL
);\n\n""") 

name = ["vrignaud","thoumelin","thoux","sy","sieurin","seillan","rossetti","robin","robert","peron","noel","mesdouri","mbasso","mathieu","masson","mammeri","malkas","madiot","lorilleux","li","lhonore","lepennec","lemercier","leger","lefeuvre","le cahain","laperdrix","langlais","lagrange","hinsinger","hammouda","guirinec","guilpain","guegant","guionnet","granger","gilles","georget","gardan","ferrand","favre","fauvet","fabry","el marzgioui","djedai","desiles","couka","chausse","charrier","carteron","brunelat","boutet","berland","berrard","berge","bergaoui","bailleul","artur","amhachi","aanor","aaron","abbon","abby","abdel","abdon","abel","abélard","abélia","abella","abigaël","abondance","abraham","acace","achille","acmé","ada","adalard","adalbert","adalric","adalsinde","adam","adama","adélaïde","adélaïs","adélard","adèle","adelice","adélie","adelin","adelind","adeline","adelphe","adelphine","adeltrude","adémar","adénora","adine","adolphe","adon","adonis","adoré"]

toWrite = ""
for i in range(0,100):
	toWrite += "INSERT INTO team VALUES("+str(i)+', "'+name[i]+'", '+str(random.randint(0,99))+", "+str(random.randint(0,99))+");\n"
f.write(toWrite)
f.close()