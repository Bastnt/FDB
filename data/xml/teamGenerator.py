import xml.etree.cElementTree as ET
import random

MOVES = 606
NB_POKEMON = 718
NICKNAMES = ["Krakatoa","Ceto","Kratos","Splinter","Nekhbet","Lucifer","Morana","Gaia","RoyalFlush","Black","Jack","Uranie","Loki","Libitina","Link","Mothra","Tekton","Maelstrom","Hedjour","Etna","M Phelps","Alpha","Briare","Nepenthes","Kraken","Goliath","Epona","Sigma","Iridium","Cyclos","Chloridrik","Malefique","Amphitrite","Eywa","Kali","Mike","Tyson","Arsenic","Macaria","Zapatta","Artemis","Crios","Hyperion","Minos","Nemesis","Neptune","Ether","Backdraft","Okeanos","Boudha","Godzilla","Demeter","Vulcain","Sobek","Sly","Ascalaphos","Cassiopee","Arianne","Nyx","Ampere","Calcaire","Hequet","Clematite","Scylla","Circee","Kappa","Sirius","Panzer","Chrome","Cerbere","Dynamite","Titane","Murphy","Atlas","Belar","Davy","Jones","Kuroshio","Mercure","Anubis","Nessy","Ganesh","Calliope","Phobos","Pluton","Europee","Aphrodite","Stonehenge","Komodo","Horus","Mississipi","Mononoke","Enlil","Nymphea","Selvans","Vaillance","Eole","Eris","Ares","Crescendo","Yokozuna","Iota","Banshee","Palladium","Typhon","Nataraja","Shiva","Thor","Ying","Yang","Romeo","Juliette","Citrik","Kàmohoali","Vesuve","Tambora","Gamma","Molotov","Kalahari","Hawortia","Xena","Kukulkan","Helios","Namazu","Charybde","Kronos","Caulerpa","Anapurna","Thetys","Espio","Thanatos","Callisto","Osiris","MrFreeze","Neree","Clio","Amethyste","Ragnarok","Apocalypse","Hephaistos","Richter","Hanuman","Poseideon","Raptor","Olympe","Aker","Myosotis","Kilauea","Oter","Ourea","Orion","Zephyr","Venus","Nightmare","Don","Corbo","Basthet","Souffre","Mjolnir","Kerta","Titan","Herakles","Opet","Heredet","Cyanure","Vidar","Odin","Circee","Shockwave","Dionysos","Gaia","Dziewona","Zeus","Agounia","Fujin","Rafale","Mirage","Rose","Metnal","Chyroptera","Everest","Windows 7","Ouranos","Granite","Charon","Bertha"]


root = ET.Element("teams")
# A hundred teams
for i in range(0,100):
	team = ET.SubElement(root, "team")
	team.set("id", str(i))
	# From 1 to 6 Pokemon per team
	for j in range(0, random.randint(1,6)):
		pokemon = ET.SubElement(team, "pokemon")
		pokemon.set("id", str(random.randint(1,NB_POKEMON)))
		# Some have a nickname
		if(random.random() > 0.5):
			nickname = ET.SubElement(pokemon,"nickname")
			nickname.text = random.choice(NICKNAMES)
		# From 1 to 4 move per Pokemon
		for k in range(0, random.randint(1,4)):
			move = ET.SubElement(pokemon, "move")
			move.set("id", str(random.randint(0, MOVES)))

# Writing of the file
tree = ET.ElementTree(root)
tree.write("teams.xml")