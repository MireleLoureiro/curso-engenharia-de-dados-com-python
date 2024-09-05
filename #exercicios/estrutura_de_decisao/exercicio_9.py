numero_1 = int(input("Digite 1º número: "))
numero_2 = int(input("Digite 2º número: "))
numero_3 = int(input("Digite 3º número: "))

numeros = [numero_1, numero_2, numero_3]
numeros.sort(reverse=True)

print(f"Números em ordem descrescente: {numeros}")