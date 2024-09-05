import math

area_pintar = float(input("Digite o tamanho em m² da área a ser pintada: "))

litros_necessarios = area_pintar / 3
latas_necessarios = math.ceil(litros_necessarios / 18)
preco_por_lata = 80.0
preco_total = latas_necessarios * preco_por_lata

print(f"Você irá precisar de {latas_necessarios} lata(s) de tinta(s)")
print(f"Preço total: R$ {preco_total:.2f}")
