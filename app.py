from random import randint
from operaciones.Operaciones import sumar,restar,multiplicar,dividir

#Se generan 3 números aleatorios entre 1 y 100:
num1 = randint(1,100)
num2 = randint(1,100)
num3 = randint(1,100)
#Se realizan las 4 operaciones matemáticas básicas con los números generados:
print(f'\n{num1} + {num2} + {num3} = {sumar(num1,num2,num3)}')
print(f'{num1} - {num2} - {num3} = {restar(num1,num2,num3)}')
print(f'{num1} * {num2} * {num3} = {multiplicar(num1,num2,num3)}')
print(f'{num1} / {num2} / {num3} = {dividir(num1,num2,num3)}')