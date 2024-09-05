numero_1 = float(input("Digite o 1º número: "))
numero_2 = float(input("Digite o 2º número: "))
numero_3 = float(input("Digite o 3º número: "))

maior = max(numero_1, numero_2, numero_3)

if numero_1 == numero_2 == numero_3:
    print("Os números são iguais!")
else:
    print(f"O maior número é: {maior}")