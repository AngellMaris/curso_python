# -*- coding: utf-8 -*-
"""Advinhacao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17lkU6xRMce8NbcGjulsGwnzRB7GrDKYD
"""

from random import randint
valor = randint(0,10)
print(valor)

from random import randint

print("-------Iniciando o Super Game ------")

tesouro = randint(0,100)
chute = 0
chances = 10

while chute != tesouro :
  chute = input("Qual número você acha que é?")
  if chute.isnumeric() : 
    chute = int(chute)
    chances = chances - 1 
    if chute == tesouro :# == significa igual
       print('')
       print('Parabéns! Você acertou')
       print('O número era {} e você ainda tinha {} chances'.format(tesouro,chances))
       print('')
       break;
    else:
        print('') 
        if chute > tesouro:
          print('Você errou! Dica; É um número menor!')
        else:
          print('Você errou! Dica: É um número maior!')  
        print('Você ainda possui {} chances'.format(chances)) 
    if chances == 0 :
         print('')  
         print(f'Suas chances acabaram. O número era:{tesouro}.Você Perdeu')
         print('')
         break;
else:
  print('')       
  print('Você inseriu letras, é apenas numeros')
  print(f'Você ainda possui {chances} chances')
  print('')
print("------- Game Over ------")