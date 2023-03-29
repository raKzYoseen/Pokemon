import random

class Pokemon:
        def __init__(self,nome,tipo,hp,ataque,defesa):
                self.nome = nome
                self.tipo = tipo
                self.hp = hp
                self.ataque = ataque
                self.defesa = defesa


        def calcularVantagens(self, oponente):
                if oponente.tipo.__name__ in self.vantagem:
                        return 2
                
                elif oponente.tipo.__name__  in self.desvantagem:
                        return 0.5
                
                elif oponente.tipo.__name__  in self.empate:
                        return 1


        

class Normal(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=[]
                self.desvantagem=['Pedra', 'Fantasma']
                self.empate=['Normal', 'Fogo', 'Agua', 'Planta', 'Eletrico', 'Gelo', 'Lutador', 'Venenoso', 'Terrestre', 'Voador', 'Psiquico', 'Inseto', 'Escuridao', 'Dragao', 'Aco', 'Fada']


class Fogo(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=['Planta', 'Gelo', 'Inseto', 'Aco']
                self.desvantagem=['Agua', 'Pedra', 'Dragao']
                self.empate=['Normal', 'Fogo', 'Eletrico', 'Lutador', 'Venenoso', 'Terrestre', 'Voador', 'Psiquico', 'Fantasma', 'Escuridao', 'Fada']     


class Agua(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo, hp,ataque, defesa)
                self.vantagem=['Fogo', 'Terrestre', 'Pedra']
                self.desvantagem=['Planta', 'Dragao']
                self.empate=['Normal', 'Agua', 'Eletrico', 'Gelo', 'Lutador', 'Venenoso', 'Voador', 'Psiquico', 'Inseto', 'Fantasma', 'Escuridao', 'Aco', 
'Fada']


class Planta(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo, hp,ataque, defesa)
                self.vantagem=['Agua', 'Terrestre', 'Pedra']
                self.desvantagem=['Fogo', 'Venenoso', 'Voador', 'Inseto', 'Dragao', 'Aco']
                self.empate=['Normal', 'Planta', 'Eletrico', 'Gelo', 'Lutador', 'Psiquico', 'Fantasma', 'Escuridao', 'Fada']


class Eletrico(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=['Agua', 'Voador']
                self.desvantagem=['Planta', 'Terrestre', 'Dragao']
                self.empate=['Normal', 'Fogo', 'Eletrico', 'Gelo', 'Lutador', 'Venenoso', 'Psiquico', 'Inseto', 'Pedra', 'Fantasma', 'Escuridao', 'Aco', 'Fada']


class Gelo(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=['Planta', 'Terrestre', 'Voador', 'Dragao']
                self.desvantagem=['Fogo', 'Agua', 'Aco']
                self.empate=['Normal', 'Eletrico', 'Gelo', 'Lutador', 'Venenoso', 'Psiquico', 'Inseto', 'Pedra', 'Fantasma', 'Escuridao', 'Fada']


class Lutador(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=['Normal', 'Gelo', 'Pedra', 'Escuridao', 'Aco']
                self.desvantagem=['Venenoso', 'Voador', 'Psiquico', 'Inseto', 'Fantasma', 'Fada']
                self.empate=['Fogo', 'Agua', 'Planta', 'Eletrico', 'Lutador', 'Terrestre', 'Dragao']


class Venenoso(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=['Planta', 'Fada']
                self.desvantagem=['Terrestre', 'Pedra', 'Fantasma', 'Aco']
                self.empate=['Normal', 'Fogo', 'Agua', 'Eletrico', 'Gelo', 'Lutador', 'Venenoso', 'Voador', 'Psiquico', 'Inseto', 'Escuridao', 'Dragao']  


class Terrestre(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=['Fogo', 'Eletrico', 'Venenoso', 'Pedra', 'Aco']
                self.desvantagem=['Planta', 'Voador', 'Inseto']
                self.empate=['Normal', 'Agua', 'Gelo', 'Lutador', 'Terrestre', 'Psiquico', 'Fantasma', 'Escuridao', 'Dragao', 'Fada']


class Voador(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo, hp,ataque, defesa)
                self.vantagem=['Planta', 'Lutador', 'Inseto']
                self.desvantagem=['Eletrico', 'Pedra', 'Aco']
                self.empate=['Normal', 'Fogo', 'Agua', 'Gelo', 'Venenoso', 'Terrestre', 'Voador', 'Psiquico', 'Fantasma', 'Escuridao', 'Dragao', 'Fada']  


class Psiquico(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=['Lutador', 'Venenoso']
                self.desvantagem=['Escuridao', 'Aco']
                self.empate=['Normal', 'Fogo', 'Agua', 'Planta', 'Eletrico', 'Gelo', 'Terrestre', 'Voador', 'Psiquico', 'Inseto', 'Pedra', 'Fantasma', 'Dragao', 'Fada']


class Inseto(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=['Planta', 'Psiquico', 'Escuridao']
                self.desvantagem=['Fogo', 'Lutador', 'Venenoso', 'Voador', 'Fantasma', 'Aco', 'Fada']
                self.empate=['Normal', 'Agua', 'Eletrico', 'Gelo', 'Terrestre', 'Inseto', 'Pedra', 'Dragao']


class Pedra(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=['Fogo', 'Gelo', 'Voador']
                self.desvantagem=['Lutador', 'Terrestre', 'Aco']
                self.empate=['Normal', 'Agua', 'Planta', 'Eletrico', 'Venenoso', 'Psiquico', 'Inseto', 'Pedra', 'Fantasma', 'Escuridao', 'Dragao', 'Fada']

class Fantasma(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo, hp,ataque, defesa)
                self.vantagem=['Psiquico']
                self.desvantagem=['Normal', 'Escuridao']
                self.empate=['Fogo', 'Agua', 'Planta', 'Eletrico', 'Gelo', 'Lutador', 'Venenoso', 'Terrestre', 'Voador', 'Inseto', 'Pedra', 'Fantasma', 'Dragao', 'Aco', 'Fada']


class Escuridao(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=['Psiquico', 'Fantasma']
                self.desvantagem=['Lutador', 'Fada']
                self.empate=['Normal', 'Fogo', 'Agua', 'Planta', 'Eletrico', 'Gelo', 'Venenoso', 'Terrestre', 'Voador', 'Inseto', 'Pedra', 'Escuridao', 'Dragao', 'Aco']


class Dragao(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=[]
                self.desvantagem=['Aco', 'Fada']
                self.empate=['Normal', 'Fogo', 'Agua', 'Planta', 'Eletrico', 'Gelo', 'Lutador', 'Venenoso', 'Terrestre', 'Voador', 'Psiquico', 'Inseto', 'Pedra', 'Fantasma', 'Escuridao', 'Dragao']


class Aco(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo, hp,ataque, defesa)
                self.vantagem=['Gelo', 'Pedra', 'Fada']
                self.desvantagem=['Fogo', 'Agua', 'Eletrico']
                self.empate=['Normal', 'Planta', 'Lutador', 'Venenoso', 'Terrestre', 'Voador', 'Psiquico', 'Inseto', 'Fantasma', 'Escuridao', 'Dragao', 'Aco']


class Fada(Pokemon):
        def __init__(self, nome, tipo, hp, ataque, defesa):
                super().__init__(nome, tipo,hp, ataque, defesa)
                self.vantagem=['Lutador', 'Escuridao', 'Dragao']
                self.desvantagem=['Fogo', 'Venenoso', 'Aco']
                self.empate=['Normal', 'Agua', 'Planta', 'Eletrico', 'Gelo', 'Terrestre', 'Voador', 'Psiquico', 'Inseto', 'Pedra', 'Fantasma', 'Fada']  


bulbasaur = (Planta)("Bulbasaur", Planta, 45, 49, 49)
ivysaur = (Planta)("Ivysaur", Planta, 60, 62, 63)   
venusaur = (Planta)("Venusaur", Planta, 82, 83, 100)
charmander = (Fogo)("Charmander", Fogo, 39, 52, 43) 
charmeleon = (Fogo)("Charmeleon", Fogo, 58, 64, 58) 
charizard = (Fogo)("Charizard", Fogo, 84, 78, 109)  
squirtle = (Agua)("Squirtle", Agua, 44, 48, 65)     
wartortle = (Agua)("Wartortle", Agua, 59, 63, 80)   
blastoise = (Agua)("Blastoise", Agua, 83, 100, 85)  
caterpie = (Inseto)("Caterpie", Inseto, 45, 30, 35) 
metapod = (Inseto)("Metapod", Inseto, 50, 20, 55)   
butterfree = (Inseto)("Butterfree", Inseto, 45, 50, 90)
weedle = (Inseto)("Weedle", Inseto, 40, 35, 30)
kakuna = (Inseto)("Kakuna", Inseto, 45, 25, 50)
beedrill = (Inseto)("Beedrill", Inseto, 90, 40, 45)
pidgey = (Normal)("Pidgey", Normal, 40, 45, 40)
pidgeotto = (Normal)("Pidgeotto", Normal, 63, 60, 55)
pidgeot = (Normal)("Pidgeot", Normal, 80, 75, 70)
rattata = (Normal)("Rattata", Normal, 30, 56, 35)
raticate = (Normal)("Raticate", Normal, 81, 60, 50)
spearow = (Normal)("Spearow", Normal, 40, 60, 30)
fearow = (Normal)("Fearow", Normal, 90, 65, 61)
ekans = (Venenoso)("Ekans", Venenoso, 35, 60, 44)
arbok = (Venenoso)("Arbok", Venenoso, 95, 69, 65)
pikachu = (Eletrico)("Pikachu", Eletrico, 55, 40, 50)
raichu = (Eletrico)("Raichu", Eletrico, 90, 55, 90)
sandshrew = (Terrestre)("Sandshrew", Terrestre, 50, 75, 85)
sandslash = (Terrestre)("Sandslash", Terrestre, 100, 110, 45)
nidoran = (Venenoso)("Nidoran♀", Venenoso, 55, 47, 52)
nidorina = (Venenoso)("Nidorina", Venenoso, 62, 67, 55)
nidoqueen = (Venenoso)("Nidoqueen", Venenoso, 92, 87, 75)
nidoran = (Venenoso)("Nidoran♂", Venenoso, 46, 57, 40)
nidorino = (Venenoso)("Nidorino", Venenoso, 72, 57, 55)
nidoking = (Venenoso)("Nidoking", Venenoso, 102, 77, 85)
clefairy = (Fada)("Clefairy", Fada, 45, 48, 60)
clefable = (Fada)("Clefable", Fada, 70, 73, 95)
vulpix = (Fogo)("Vulpix", Fogo, 41, 40, 50)
ninetales = (Fogo)("Ninetales", Fogo, 76, 75, 81)
jigglypuff = (Normal)("Jigglypuff", Normal, 45, 20, 45)
wigglytuff = (Normal)("Wigglytuff", Normal, 70, 45, 85)
zubat = (Venenoso)("Zubat", Venenoso, 40, 45, 35)
golbat = (Venenoso)("Golbat", Venenoso, 80, 70, 65)
oddish = (Planta)("Oddish", Planta, 45, 50, 55)
gloom = (Planta)("Gloom", Planta, 65, 70, 85)
vileplume = (Planta)("Vileplume", Planta, 80, 85, 110)
paras = (Inseto)("Paras", Inseto, 35, 70, 55)
parasect = (Inseto)("Parasect", Inseto, 95, 80, 60)
venonat = (Inseto)("Venonat", Inseto, 60, 55, 50)
venomoth = (Inseto)("Venomoth", Inseto, 65, 60, 90)
diglett = (Terrestre)("Diglett", Terrestre, 10, 55, 25)
dugtrio = (Terrestre)("Dugtrio", Terrestre, 100, 50, 50)
meowth = (Normal)("Meowth", Normal, 40, 45, 35)
persian = (Normal)("Persian", Normal, 70, 60, 65)
psyduck = (Agua)("Psyduck", Agua, 50, 52, 48)
golduck = (Agua)("Golduck", Agua, 82, 78, 95)
mankey = (Lutador)("Mankey", Lutador, 40, 80, 35)
primeape = (Lutador)("Primeape", Lutador, 105, 60, 60)
growlithe = (Fogo)("Growlithe", Fogo, 70, 45, 70)
arcanine = (Fogo)("Arcanine", Fogo, 110, 80, 100)
poliwag = (Agua)("Poliwag", Agua, 40, 50, 40)
poliwhirl = (Agua)("Poliwhirl", Agua, 65, 65, 50)
poliwrath = (Agua)("Poliwrath", Agua, 95, 95, 70)
abra = (Psiquico)("Abra", Psiquico, 25, 20, 15)
kadabra = (Psiquico)("Kadabra", Psiquico, 35, 30, 120)
alakazam = (Psiquico)("Alakazam", Psiquico, 50, 45, 135)
machop = (Lutador)("Machop", Lutador, 70, 80, 50)
machoke = (Lutador)("Machoke", Lutador, 100, 70, 50)
machamp = (Lutador)("Machamp", Lutador, 130, 80, 65)
bellsprout = (Planta)("Bellsprout", Planta, 50, 75, 35)
weepinbell = (Planta)("Weepinbell", Planta, 90, 50, 85)
victreebel = (Planta)("Victreebel", Planta, 105, 65, 100)
tentacool = (Agua)("Tentacool", Agua, 40, 40, 35)
tentacruel = (Agua)("Tentacruel", Agua, 70, 65, 80)
geodude = (Pedra)("Geodude", Pedra, 40, 80, 100)
graveler = (Pedra)("Graveler", Pedra, 95, 115, 45)
golem = (Pedra)("Golem", Pedra, 120, 130, 55)
ponyta = (Fogo)("Ponyta", Fogo, 50, 85, 55)
rapidash = (Fogo)("Rapidash", Fogo, 100, 70, 80)
slowpoke = (Agua)("Slowpoke", Agua, 90, 65, 65)
slowbro = (Agua)("Slowbro", Agua, 75, 110, 100)
magnemite = (Eletrico)("Magnemite", Eletrico, 25, 35, 70)
magneton = (Eletrico)("Magneton", Eletrico, 60, 95, 120)
farfetch = (Normal)("Farfetch'd", Normal, 90, 55, 58)
doduo = (Normal)("Doduo", Normal, 35, 85, 45)
dodrio = (Normal)("Dodrio", Normal, 110, 70, 60)
seel = (Agua)("Seel", Agua, 65, 45, 55)
dewgong = (Agua)("Dewgong", Agua, 70, 80, 70)
grimer = (Venenoso)("Grimer", Venenoso, 80, 80, 50)
muk = (Venenoso)("Muk", Venenoso, 105, 75, 65)
shellder = (Agua)("Shellder", Agua, 65, 100, 45)
cloyster = (Agua)("Cloyster", Agua, 95, 180, 85)
gastly = (Fantasma)("Gastly", Fantasma, 30, 35, 30)
haunter = (Fantasma)("Haunter", Fantasma, 50, 45, 115)
gengar = (Fantasma)("Gengar", Fantasma, 65, 60, 130)
onix = (Pedra)("Onix", Pedra, 45, 160, 30)
drowzee = (Psiquico)("Drowzee", Psiquico, 60, 48, 45)
hypno = (Psiquico)("Hypno", Psiquico, 73, 70, 73)
krabby = (Agua)("Krabby", Agua, 30, 105, 90)
kingler = (Agua)("Kingler", Agua, 130, 115, 50)
voltorb = (Eletrico)("Voltorb", Eletrico, 40, 30, 50)
electrode = (Eletrico)("Electrode", Eletrico, 50, 70, 80)
exeggcute = (Planta)("Exeggcute", Planta, 40, 80, 60)
exeggutor = (Planta)("Exeggutor", Planta, 95, 85, 125)
cubone = (Terrestre)("Cubone", Terrestre, 50, 50, 95)
marowak = (Terrestre)("Marowak", Terrestre, 80, 110, 50)
hitmonlee = (Lutador)("Hitmonlee", Lutador, 120, 53, 35)
hitmonchan = (Lutador)("Hitmonchan", Lutador, 105, 79, 35)
lickitung = (Normal)("Lickitung", Normal, 55, 75, 60)
koffing = (Venenoso)("Koffing", Venenoso, 40, 65, 95)
weezing = (Venenoso)("Weezing", Venenoso, 90, 120, 85)
rhyhorn = (Terrestre)("Rhyhorn", Terrestre, 80, 85, 95)
rhydon = (Terrestre)("Rhydon", Terrestre, 130, 120, 45)
chansey = (Normal)("Chansey", Normal, 5, 5, 35)
tangela = (Planta)("Tangela", Planta, 55, 115, 100)
kangaskhan = (Normal)("Kangaskhan", Normal, 95, 80, 40)
horsea = (Agua)("Horsea", Agua, 30, 40, 70)
seadra = (Agua)("Seadra", Agua, 65, 95, 95)
goldeen = (Agua)("Goldeen", Agua, 45, 67, 60)
seaking = (Agua)("Seaking", Agua, 92, 65, 65)
staryu = (Agua)("Staryu", Agua, 45, 55, 70)
starmie = (Agua)("Starmie", Agua, 75, 85, 100)
mrmime = (Psiquico)("Mr. Mime", Psiquico, 45, 65, 100)
scyther = (Inseto)("Scyther", Inseto, 110, 80, 55)
jynx = (Gelo)("Jynx", Gelo, 50, 35, 115)
electabuzz = (Eletrico)("Electabuzz", Eletrico, 83, 57, 95)
magmar = (Fogo)("Magmar", Fogo, 95, 57, 100)
pinsir = (Inseto)("Pinsir", Inseto, 125, 100, 55)
tauros = (Normal)("Tauros", Normal, 100, 95, 40)
magikarp = (Agua)("Magikarp", Agua, 20, 10, 55)
gyarados = (Agua)("Gyarados", Agua, 125, 79, 60)
lapras = (Agua)("Lapras", Agua, 85, 80, 85)
ditto = (Normal)("Ditto", Normal, 48, 48, 48)
eevee = (Normal)("Eevee", Normal, 55, 50, 45)
vaporeon = (Agua)("Vaporeon", Agua, 65, 60, 110)
jolteon = (Eletrico)("Jolteon", Eletrico, 65, 60, 110)
flareon = (Fogo)("Flareon", Fogo, 130, 60, 95)
porygon = (Normal)("Porygon", Normal, 60, 70, 85)
omanyte = (Pedra)("Omanyte", Pedra, 35, 40, 100)
omastar = (Pedra)("Omastar", Pedra, 60, 125, 115)
kabuto = (Pedra)("Kabuto", Pedra, 30, 80, 90)
kabutops = (Pedra)("Kabutops", Pedra, 115, 105, 65)
aerodactyl = (Pedra)("Aerodactyl", Pedra, 105, 65, 60)
snorlax = (Normal)("Snorlax", Normal, 110, 65, 65)
articuno = (Gelo)("Articuno", Gelo, 85, 100, 95)
zapdos = (Eletrico)("Zapdos", Eletrico, 90, 85, 125)
moltres = (Fogo)("Moltres", Fogo, 100, 90, 125)
dratini = (Dragao)("Dratini", Dragao, 41, 64, 45)
dragonair = (Dragao)("Dragonair", Dragao, 61, 84, 65)
dragonite = (Dragao)("Dragonite", Dragao, 134, 95, 100)
mewtwo = (Psiquico)("Mewtwo", Psiquico, 110, 90, 154)
mew = (Psiquico)("Mew", Psiquico, 100, 100, 100)


pokemons = [bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise, caterpie, metapod, butterfree, weedle, kakuna, beedrill, pidgey, pidgeotto, pidgeot, rattata, raticate, spearow, fearow, ekans, arbok, pikachu, raichu, sandshrew, sandslash, nidoran, nidorina, nidoqueen, nidoran, nidorino, nidoking, clefairy, clefable, vulpix, ninetales, jigglypuff, wigglytuff, zubat, golbat, oddish, gloom, vileplume, paras, parasect, venonat, venomoth, diglett, dugtrio, meowth, persian, psyduck, golduck, mankey, primeape, growlithe, arcanine, poliwag, poliwhirl, poliwrath, abra, kadabra, alakazam, machop, machoke, machamp, bellsprout, weepinbell, victreebel, tentacool, tentacruel, geodude, graveler, golem, ponyta, rapidash, slowpoke, slowbro, magnemite, magneton, farfetch, doduo, dodrio, seel, dewgong, grimer, muk, shellder, cloyster, gastly, haunter, gengar, onix, drowzee, hypno, krabby, kingler, voltorb, electrode, exeggcute, exeggutor, cubone, marowak, hitmonlee, hitmonchan, lickitung, koffing, weezing, rhyhorn, rhydon, chansey, tangela, kangaskhan, horsea, seadra, goldeen, seaking, staryu, starmie, mrmime, scyther, jynx, electabuzz, magmar, pinsir, tauros, magikarp, gyarados, lapras, ditto, eevee, vaporeon, jolteon, flareon, porygon, omanyte, omastar, kabuto, kabutops, aerodactyl, snorlax, articuno, zapdos, moltres, dratini, dragonair, dragonite, mewtwo, mew]
iniciais = [bulbasaur, charmander, squirtle]
