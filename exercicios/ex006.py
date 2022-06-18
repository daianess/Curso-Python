# Exercício 006 - Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é {} \nO triplo é {} e \nA raiz quadrada é {:.2f}' .format(n, d, t, r))

# ============================================== OU ============================================= #

n = int(input('Digite um número: '))
print('O dobro de {} é {} \nO triplo é {} e \nA raiz quadrada é {:.2f}' .format(n, (n*2), (n*3), (n**(1/2))))

# ============================================== OU ============================================= #

n = int(input('Digite um número: '))
print('O dobro de {} é {} \nO triplo é {} e \nA raiz quadrada é {:.2f}' .format(n, (n*2), (n*3), pow(n, (1/2))))
