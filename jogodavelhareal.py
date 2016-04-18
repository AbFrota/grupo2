#
#Introdução a Programação de Computadores
#Professor: Jucimar JR
#EQUIPE 2
#
#Ana Beatriz Frota  - 1615310027 
#Ariel Guilherme Rocha Capistrano - 1615310029
#Franklin Yuri Gonçaves dos santos - 1615310033
#Kylciane Cristiny Lopes Freitas - 1615310052
#Lucas Ferreira Soares - 1615310014
#Luiz Alexandre Oliveira de Souza - 1615310057
#Luiz Gustavo Rocha Melo - 1615310015
#Nahan Trindade Passos - 1615310021
#Samuel Silva França - 1615310049

def imprimeCampo(campo):
        c = 0
        for i in campo:
                if c % 3 == 0:
                        print ""
                        c = 0
                print i,
                c += 1    
        print "\n"

def ganhou(simbolo, campo):
        #teste horizontal
        if ((campo[0] == simbolo) and (campo[1] == simbolo) and (campo[2] == simbolo)) or ((campo[3] == simbolo) and (campo[4] == simbolo) and (campo[5] == simbolo))or ((campo[6] == simbolo) and (campo[7] == simbolo) and (campo[8] == simbolo)):
                return 1
        #fim horizontal
        
        #teste vertical
        if ((campo[0] == simbolo) and (campo[3] == simbolo) and (campo[6] == simbolo)) or ((campo[1] == simbolo) and (campo[4] == simbolo) and (campo[7] == simbolo))or ((campo[2] == simbolo) and (campo[5] == simbolo) and (campo[8] == simbolo)):
                return 1
        #fim vertical
        
        #teste diagonal
        if ((campo[0] == simbolo) and (campo[4] == simbolo) and (campo[8] == simbolo)) or ((campo[2] == simbolo) and (campo[4] == simbolo) and (campo[6] == simbolo)):
                return 1
        #fim diagonal

def velha(campo):
        if '_' not in campo:
                return 1
        

import random

campo = ['_','_','_','_','_','_','_','_','_']

jogador = random.choice((0,1))
jogador_1 = raw_input('\nQual o seu nome?: ')
jogador_2 = raw_input('\nDe um nome ao seu oponente (PC): ')


if jogador == 1:
        a = 'X'
        b = 'O'
else:
        b = 'X'
        a = 'O'

print ("\nSeu simbolo é %s" % a)
print ("\nO simbolo do Pc é %s" % b)

print """\n              Posições
              0 | 1 | 2  
             ---+---+---
              3 | 4 | 5 
             ---+---+---
              6 | 7 | 8 """

while 1:
        if velha(campo):
                imprimeCampo(campo)
                print ("Ops, o jogo velhou!")
                break
        if jogador:
                imprimeCampo(campo)
                
                while 1:
                        print """\n              
                Posições
                0 | 1 | 2  
               ---+---+---
                3 | 4 | 5 
               ---+---+---
                6 | 7 | 8 """
                        
                        vc = int(raw_input("Digite sua posicao: "))                      
                        if campo[vc] == '_':                
                                break

                campo[vc] = a
                jogador = 0               

                if ganhou(a,campo):
                        imprimeCampo(campo)
                        print ("Parabens voce ganhou :) ")
                        break

        else:
                imprimeCampo(campo)
                while 1:
                        pc = random.randint(0,8)
                        
                        if campo[pc] == '_':
                                break

                campo[pc] = b
        
                jogador = 1
        
                if ganhou(b,campo):
                        imprimeCampo(campo)
                        print ("Nao foi dessa vez, o PC ganhou!")
                        break