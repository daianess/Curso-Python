# Exercício 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Digite uma distância em metros: '))
cm = metro * 100
mm = metro * 1000
print('O valor de {}m em centímetro é de {:.0f}cm e em milímetro é de {:.0f}mm' .format(metro, cm, mm))