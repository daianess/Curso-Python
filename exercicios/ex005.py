# Exercício 005 - Faça um programa que leia um número Inteiro e mostre na tela seu sucessor e seu antecessor.

numero = int(input('Digite um número: '))
s = numero + 1
a = numero - 1
print('Analisando o número {}, \nSeu sucessor é {} e \nO antecessor é {}' .format(numero, s, a))

# ============================================== OU ============================================= #

n = int(input('Digite um número: '))
print('Analisando o número {}, seu sucessor é {} e o antecessor é {}' .format(n, (n+1), (n-1)))