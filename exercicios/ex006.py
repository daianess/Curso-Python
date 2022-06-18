# Exercício 006 - Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print('O dobro de {} é {} \nO triplo é {} e \nA raiz quadrada é {:.2f}' .format(numero, dobro, triplo, raiz))

# ============================================== OU ============================================= #

n = int(input('Digite um número: '))
print('O dobro de {} é {} \nO triplo é {} e \nA raiz quadrada é {:.2f}' .format(n, (n*2), (n*3), (n**(1/2))))

# ============================================== OU ============================================= #

n = int(input('Digite um número: '))
print('O dobro de {} é {} \nO triplo é {} e \nA raiz quadrada é {:.2f}' .format(n, (n*2), (n*3), pow(n, (1/2))))
