from pokemon import *
from treinador import *
import os


treinador1.escolherPokemonInicial()
while True:
    print(f'''\n\n        Menu
        1 - Batalhar!
        2 - Exibir Pokemons na Mochila!
        3 - Sair!''')
    try:
        escolha = int(input('> '))

        if escolha == 1:
            os.system('cls')
            treinador1.batalha(oponente1.escolherPokemonInimigo())

        elif escolha == 2:
            os.system('cls')
            treinador1.listarPokemons()
            os.system('cls')
        
        elif escolha == 3:
            os.system('cls')
            break
        

    except ValueError:
        print('Valor Invalido')
        os.system('cls')
