# Exercício 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite uma distância em metros: '))
cm = m * 100
mm = m * 1000
print('O valor de {}m em centímetro é de {:.0f}cm e em milímetro é de {:.0f}mm' .format(m, cm, mm))