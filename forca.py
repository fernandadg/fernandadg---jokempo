# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:23:20 2015

@author: david
"""

import turtle
import random
import time

o = open("entrada.txt", encoding="utf-8")
r = o.readlines()

lista = []
for ln in r:
    c = ln.strip()
    if c != "":
        lista.append(c)
print(lista)

n= len(lista) - 1
pn = random.randint(0,n)
palavra = lista[pn]
palavram = palavra.upper()
print(palavra) 
x= len(palavra)

espaco = []
start = 0
while start != -1:
    start = palavra.find(" ", start)
    espaco.append(start)
    if start != -1:
        start += 1
del espaco[-1]
del lista[pn]

tela = turtle.Screen() 
tela.bgcolor("hotpink")

tartaruga1 = turtle.Turtle()
tartaruga1.pen(shown =False,fillcolor="black",pencolor="black")
tartaruga1.penup()

tartaruga2 = turtle.Turtle()
tartaruga2.speed(10)
tartaruga2.pen(shown =False,fillcolor="black",pencolor="black")
tartaruga2.penup()
tartaruga2.setpos(-350, 10)
tartaruga2.color("pink")

tartaruga3 = turtle.Turtle()
tartaruga3.penup()
tartaruga3.pen(shown =False,fillcolor="deeppink",pencolor="deeppink")
tartaruga3.pensize(4)
tartaruga3.setpos(-250, -250)
tartaruga3.pendown()
tartaruga3.left(90)
tartaruga3.forward(400)
tartaruga3.right(90)
tartaruga3.forward(100)
tartaruga3.right(90)
tartaruga3.forward(55)
tartaruga3.penup()

tartaruga4 = turtle.Turtle()
tartaruga4.pen(shown =False,fillcolor="black",pencolor="black")

tartaruga5 = turtle.Turtle()
tartaruga5.penup()
tartaruga5.pen(shown =False,fillcolor="pink",pencolor="pink")

letras = []
i = 0
t = 0

while t != x:
    letras.append(palavra[t].upper())
    t += 1

while i != x:
    tartaruga2.setpos(i*30-x*15,-100)
    if palavra[i] == " " :
        tartaruga2.write(" ", False, align="left",font=("Arial",30))
    else:
        tartaruga2.write("_ ", False, align="left",font=("Arial",30))
    i +=1

acertos = 0
erros = 0
tentativas = []

teste = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
teste2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

e1 = 0
e2 = 0
e3 = 0
e4 = 0
e5 = 0 
e6 = 0
 
while acertos < x-len(espaco) and erros != 6:
    if erros != 6:
        chute = tela.textinput("Tentativa", "Qual a letra?")
        chutem = chute.upper()
        
        if chutem in tentativas:                        
               tartaruga4.write("Ja inserido", False, align="center",font=("Arial",40))
               time.sleep(1)
               tartaruga4.clear()
                                          
        if chutem in letras and chutem in teste and len(chute) == 1 and chutem not in tentativas:                
                tentativas.append(chutem)
                n = 0                        
                iguais = []                                                
                print("Parabens!")
                
                while n < len(palavra):                                  
                    if letras[n] == chutem:                                                                                              
                        tartaruga1.setpos(n*34-x*15,-90)                
                        tartaruga1.write(chutem, False, align="center",font=("Arial",20))            
                        acertos += 1                                                                        
                    n +=1
                    
        elif chutem not in tentativas and chute  in teste2:
                erros += 1
                tentativas.append(chutem)
                print("Opa!")
                print(erros)                       
                        
        if erros == 1 and e1 == 0: 
            tartaruga5.penup()
            tartaruga5.setpos(-150 , 55)
            tartaruga5.pendown()
            tartaruga5.circle(20)
            e1 = 1
    
        if erros == 2 and e2 == 0:
            tartaruga5.penup()
            tartaruga5.setpos(-150 , 55)
            tartaruga5.pendown()
            tartaruga5.right(90)
            tartaruga5.forward(80)
            e2 = 1            
            
        if erros == 3 and e3 == 0:
            tartaruga5.penup()
            tartaruga5.setpos(-150 , 40)
            tartaruga5.pendown()
            tartaruga5.right(30)
            tartaruga5.forward(30)
            e3 = 1
                        
        if erros == 4 and e4 == 0:
            tartaruga5.penup()
            tartaruga5.setpos(-150 , 40)
            tartaruga5.pendown()
            tartaruga5.left(80)
            tartaruga5.forward(30)
            e4 = 1
            
        if erros == 5 and e5 == 0:
            tartaruga5.penup()
            tartaruga5.setpos(-150 , -25)
            tartaruga5.pendown()
            tartaruga5.right(80)
            tartaruga5.forward(30)
            e5 = 1
            
        if erros == 6 and e6 == 0:
            tartaruga5.penup()
            tartaruga5.setpos(-150 , -25)
            tartaruga5.pendown()
            tartaruga5.left(60)
            tartaruga5.forward(30)
            e6 = 1
                        
        if acertos == x-len(espaco):
            tartaruga4.write("Parabens!", False, align="center",font=("Arial",70))
    
        if erros > 5:    
            print("Morreu!")
            tartaruga4.write("Morreu!", False, align="center",font=("Arial",80))
   
tela.exitonclick()