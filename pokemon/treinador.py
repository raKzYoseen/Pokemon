import random
from pokemon import *
import os


class Treinador:
    def __init__(self,nome):
        self.nome = nome

    def batalha(self, oponente):
        total = self.principal[0].hp + self.principal[0].ataque + self.principal[0].defesa
        multiplicador = int(Pokemon.calcularVantagens(self.principal[0], oponente))
        total = total * multiplicador
        
        total1 = oponente.hp + oponente.ataque + oponente.defesa
        total1 = total1

        print(f'{self.principal[0].nome} Vs {oponente.nome}')
        print(f'{self.principal[0].tipo.__name__} Vs {oponente.tipo.__name__}')
        print(f'Quem ganhara essa batalha???!!!')
        input()
        print(f'{self.principal[0].nome} possui {total} de dano {oponente.nome} possui {total1} de dano')
        
        if total > total1:
                print('Você ganhou!')
                treinador1.capturar(oponente)
                
        elif total < total1:
                print('Você perdeu!')
        
        elif total == total1:
                print('Empate!')
            

    def capturar(self, oponente):
        print(f'''Quer capturar {oponente.nome}?
        1 - Sim
        2 - Não''')
        escolha = int(input('> '))
        if escolha == 1:
            self.mochila.append(oponente)
            print(f'Você capturou {oponente.nome}')
        else:
            print('')

    def nomeJogador():
         os.system('cls')
         return input('Um novo treinador! Me diga seu nome:\n')
         
        
class Jogador(Treinador):
    def __init__(self, nome, mochila, principal):
        super().__init__(nome)
        self.mochila = mochila
        self.principal = principal

    def escolherPokemonInicial(self):
        os.system('cls')
        while True:
            print(f'''
            Olá {self.nome}! Escolha o seu Pokemon inicial!
            1 - Charmander
            2 - Bulbasaur
            3 - Squirtle
            ''')
            try:
                escolha = int(input('> '))
                if escolha == 1:
                    self.principal.insert(0,charmander)
                    self.mochila.append(charmander)
                    os.system('cls')
                    print(f'Parabéns! Você acaba de escolher o {charmander.nome}!')
                    break
                
                elif escolha == 2:
                    self.principal.insert(0,bulbasaur)
                    self.mochila.append(bulbasaur)
                    break
                elif escolha == 3:
                    self.principal.insert(0,squirtle)
                    self.mochila.append(squirtle)
                    break
            except ValueError:
                print('Valor Invalido')

    def listarPokemons(self):
        print('Lista de Pokemons!')
        for i, nome in enumerate(self.mochila):
            print(f'{i+1} - {nome.nome}')
        print('Escolha seus Pokemon Principal!')
        try:
            escolha = int(input('> '))
            if escolha != 0:
                self.principal.insert(0, self.mochila[escolha-1])
            else:
                print('Valor Invalido')
        except:
            print('Valor Invalido')
             


class Inimigo(Treinador):
    def __init__(self, nome):
        super().__init__(nome)

    def escolherPokemonInimigo(self):
        return random.choice(pokemons)
    
    
principal = []
mochila = []
treinador1 = Jogador(Treinador.nomeJogador(), principal, mochila)
oponente1 = Inimigo('Equipe Rocket')
# print(oponente1.escolherPokemonInimigo())
# treinador1.escolherPokemonInicial()