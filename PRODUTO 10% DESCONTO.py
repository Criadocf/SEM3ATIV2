#Escreva um programa de leia o preço de um produto e mostre na tela o valor com 10% de desconto arredondado
#para duas casas decimais.

p = float(input())
d = (p-10/100*p)
print(f'{d:.2f}')