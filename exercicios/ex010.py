# Exercício 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (Considere US$ 1,00 = R$ 3,27)

n = float(input('Quanto dinheiro você tem na sua carteira? '))
print('Com o valor de R$ {} você conseguiria comprar US$ {:.2f}' .format(n, (n/3.27)))

# ============================================== OU ============================================= #

real = float(input('Qunato dinheiro você tem na carteira? R$ '))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}' .format(real, dolar))