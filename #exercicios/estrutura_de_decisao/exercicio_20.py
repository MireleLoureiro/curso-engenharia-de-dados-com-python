nota_1 = float(input("Digite a 1ª nota: "))
nota_2 = float(input("Digite a 2ª nota: "))
nota_3 = float(input("Digite a 3ª nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media == 10.0:
    print(f"Aprovado com Distinção! Média: {media:.2f}")
elif media >= 7.0:
    print(f"Aprovado! Média: {media:.2f}")
else:
    print(f"Reprovado! Média: {media:.2f}")