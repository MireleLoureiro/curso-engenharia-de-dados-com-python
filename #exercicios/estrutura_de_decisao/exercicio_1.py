numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))

if numero_1 > numero_2:
    print(f"O maior número é: {numero_1}")
elif numero_2 > numero_1:
    print(f"O maior número é: {numero_2}")
else:
    print("Os dois números são iguais.")