# Exercício 009 - Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Digite um número: '))
m1 = numero * 1
m2 = numero * 2
m3 = numero * 3
m4 = numero * 4
m5 = numero * 5
m6 = numero * 6
m7 = numero * 7
m8 = numero * 8
m9 = numero * 9
m10 = numero * 10
print('A tabuada de', numero, 'é igual a:')
print('{} x 1 = {} ' .format(numero, m1))
print('{} x 2 = {} ' .format(numero, m2))
print('{} x 3 = {} ' .format(numero, m3))
print('{} x 4 = {} ' .format(numero, m4))
print('{} x 5 = {} ' .format(numero, m5))
print('{} x 6 = {} ' .format(numero, m6))
print('{} x 7 = {} ' .format(numero, m7))
print('{} x 8 = {} ' .format(numero, m8))
print('{} x 9 = {} ' .format(numero, m9))
print('{} x 10 = {} ' .format(numero, m10))


# ============================================== OU ============================================= #

n = int(input('Digite um número para ver a tabuada: '))
print('-' * 12)
print('{} x {:2} = {}' .format(n, 1, n*1))
print('{} x {:2} = {}' .format(n, 2, n*2))
print('{} x {:2} = {}' .format(n, 3, n*3))
print('{} x {:2} = {}' .format(n, 4, n*4))
print('{} x {:2} = {}' .format(n, 5, n*5))
print('{} x {:2} = {}' .format(n, 6, n*6))
print('{} x {:2} = {}' .format(n, 7, n*7))
print('{} x {:2} = {}' .format(n, 8, n*8))
print('{} x {:2} = {}' .format(n, 9, n*9))
print('{} x {:2} = {}' .format(n, 10, n*10))
print('-' * 12)
