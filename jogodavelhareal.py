
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
        if campo[0] == simbolo and campo[1] == simbolo and campo[2] == simbolo:
                return 1

        if campo[3] == simbolo and campo[4] == simbolo and campo[5] == simbolo:
                return 1

        if campo[6] == simbolo and campo[7] == simbolo and campo[8] == simbolo:
                return 1

        if campo[0] == simbolo and campo[3] == simbolo and campo[6] == simbolo:
                return 1

        if campo[1] == simbolo and campo[4] == simbolo and campo[7] == simbolo:
                return 1
        
        if campo[2] == simbolo and campo[5] == simbolo and campo[8] == simbolo:
                return 1

        if campo[0] == simbolo and campo[4] == simbolo and campo[8] == simbolo:
                return 1

        if campo[2] == simbolo and campo[4] == simbolo and campo[6] == simbolo:
                return 1

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