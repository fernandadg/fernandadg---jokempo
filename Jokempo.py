# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:09:28 2015

@author: david
"""

from random import choice
opc = ["pedra", "papel", "tesoura", "lagarto", "spock"]
pedra = "pedra"
papel = "papel"
tesoura = "tesoura"
lagarto = "lagarto"
spock = "spock"
#variavel1 eh o computador variavel 2 eh o jogador
variavel1=0
variavel2=0
while variavel1<3 and variavel2<3:
    computer = choice (opc)
    voce = str(input("vamos brincar de jokempo! escolha: pedra, papel, tesoura, lagarto ou spock?\n"))
    if computer == voce:
     print ("ixi, deu empate")
     print ("o computador escolheu:", computer)
    if computer == "tesoura" and (voce == "papel" or voce == "lagarto"):
     print ("poxa, o computador ganhou!")
     print ("ele escolheu:", computer)
     variavel1+=1
    if computer == "papel" and (voce == "pedra" or voce == "spock"):
     print ("poxa, o computador ganhou!")
     print ("ele escolheu:", computer)
     variavel1+=1
    if computer == "pedra" and (voce == "lagarto" or voce == "tesoura"):
     print ("poxa, o computador ganhou!")
     print ("ele escolheu:", computer)
     variavel1+=1
    if computer == "lagarto" and (voce == "spock" or voce == "papel"):
     print ("poxa, o computador ganhou!")
     print ("ele escolheu:", computer)
     variavel1+=1
    if computer == "spock" and (voce == "tesoura" or voce == "pedra"):
     print ("poxa, o computador ganhou!")
     print ("ele escolheu:", computer)
     variavel1+=1
    if voce == "tesoura" and (computer == "papel" or computer == "lagarto"):
     print ("boa, voce ganhou!")
     print ("o computador escolheu:", computer)
     variavel2+=1
    if voce == "papel" and (computer == "pedra" or computer == "spock"):
     print ("boa, voce ganhou!")
     print ("o computador escolheu:", computer)
     variavel2+=1
    if voce == "pedra" and (computer == "lagarto" or computer == "tesoura"):
     print ("boa, voce ganhou!")
     print ("o computador escolheu:", computer)
     variavel2+=1
    if voce == "lagarto" and (computer == "spock" or computer == "papel"):
     print ("boa, voce ganhou!")
     print ("o computador escolheu:", computer)
     variavel2+=1
    if voce == "spock" and (computer == "tesoura" or computer == "pedra"):
     print ("boa, voce ganhou!")
     print ("o computador escolheu:", computer)
     variavel2+=1
     
#fim do jogo     quando alguem atinge 3 pontos primeiro  
if variavel1 == 3:
 print("o computdor atingiu 3 pontos, voce perdeu!")
if variavel2 == 3:
 print("voce atingiu 3 pontos, parabens!")     
    
     