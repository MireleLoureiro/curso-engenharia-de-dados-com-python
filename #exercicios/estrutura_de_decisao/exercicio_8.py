preco_1 = float(input("Digite o preço do 1º produto: R$ "))
preco_2 = float(input("Digite o preço do 2º produto: R$ "))
preco_3 = float(input("Digite o preço do 3º produto: R$ "))

menor_valor = min(preco_1, preco_2, preco_3)

if preco_1 == preco_2 == preco_3:
    print("Produtos com o mesmo preço.")
else:
    print(f"O produço que deve comprar com o preço mais barato é o de {menor_valor:.2f}")