import xml.etree.cElementTree as ET
import random

MOVES = 606
NB_POKEMON = 718
NICKNAMES = ["Krakatoa","Céto","Kratos","Splinter","Nekhbet","Lucifer","Morana","Gaïa","RoyalFlush","Black","Jack","Uranie","Loki","Libitina","Link","Mothra","Tekton","Maëlstrom","Hedjour","Etna","M.Phelps","Alpha","Briaré","Nepenthès","Kraken","Goliath","Epona","Sigma","Iridium","Cyclos","Chloridrik","Maléfique","Amphitrite","Eywa","Kâlî","Mike","Tyson","Arsenic","Macaria","Zapatta","Artemis","Crios","Hypérion","Minos","Nemesis","Neptune","Ether","Backdraft","Okeanos","Boudha","Godzilla","Demeter","Vulcain","Sobek","Sly","Ascalaphos","Cassiopée","Arianne","Nyx","Ampère","Calcaire","Hequet","Clematite","Scylla","Circée","Kappa","Sirius","Panzer","Chrome","Cerbère","Dynamite","Titane","Murphy","Atlas","Belar","Davy","Jones","Kuroshio","Mercure","Anubis","Nessy","Ganesh","Calliope","Phobos","Pluton","Europée","Aphrodite","Stonehenge","Komodo","Horus","Mississipi","Mononoké","Enlil","Nymphéa","Selvans","Vaillance","Eole","Eris","Arès","Crescendo","Yokozuna","Iota","Banshee","Palladium","Typhon","Nataraja","Shiva","Thor","Ying","Yang","Roméo","Juliette","Citrik","Kàmohoali","Vésuve","Tambora","Gamma","Molotov","Kalahari","Hawortia","Xena","Kukulkan","Helios","Namazu","Charybde","Kronos","Caulerpa","Anapurna","Thétys","Espio","Thanatos","Callisto","Osiris","MrFreeze","Nérée","Clio","Améthyste","Ragnarok","Apocalypse","Héphaïstos","Richter","Hanuman","Poseideon","Raptor","Olympe","Aker","Myosotis","Kilauea","Oter","Ouréa","Orion","Zéphyr","Venus","Nightmare","Don","Corbo","Basthet","Souffre","Mjolnir","Kerta","Titan","Heraklès","Opet","Heredèt","Cyanure","Vidar","Odin","Circée","Shockwave","Dionysos","Gaïa","Dziewona","Zeus","Agounia","Fujin","Rafale","Mirage","Rose","Metnal","Chyroptera","Everest","Windows 7","Ouranos","Granite","Charon","Bërtha"]


root = ET.Element("teams")
# A hundred teams
for i in range(0,100):
	team = ET.SubElement(root, "team")
	team.set("id", str(i))
	# From 1 to 6 Pokémon per team
	for j in range(0, random.randint(0,5)):
		pokemon = ET.SubElement(team, "pokemon")
		pokemon.set("id", str(random.randint(1,NB_POKEMON)))
		# Some have a nickname
		if(random.random() > 0.5):
			nickname = ET.SubElement(pokemon,"nickname")
			nickname.text = random.choice(NICKNAMES)
		# From 1 to 4 move per Pokémon
		for k in range(0, random.randint(0,3)):
			move = ET.SubElement(pokemon, "move")
			move.set("id", str(random.randint(0, MOVES)))

# Writing of the file
tree = ET.ElementTree(root)
tree.write("teams.xml")
