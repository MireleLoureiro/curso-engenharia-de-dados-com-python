import math

numero_1 = int(input("Digite um número inteiro: "))
numero_2 = int(input("Digite mais um número inteiro: "))
numero_3 = float(input("Agora digite um número real: "))

produto = (2 * numero_1) * (numero_2 / 2)
soma = (3 * numero_1) + numero_3
potencia = math.pow(numero_3, 3)

print(f"O produto do dobro do primeiro com metade do segundo = {produto}")
print(f"A soma do triplo do primeiro com o terceiro = {soma}")
print(f"O terceiro elevado ao cubo = {potencia}")