import math

area_pintar = float(input("Digite o tamanho em m² da área a ser pintada: "))

litros_necessarios = area_pintar / 6
litros_necessarios *= 1.10

latas_18 = math.ceil(litros_necessarios / 18)
preco_latas_18 = latas_18 * 80.00

galoes_3_6 = math.ceil(litros_necessarios / 3.6)
preco_galoes_3_6 = galoes_3_6 * 25.00

latas_mistura = int(litros_necessarios // 18)
resto_mistura = litros_necessarios % 18
galoes_mistura = math.ceil(resto_mistura / 3.6)
preco_mistura = (latas_mistura * 80.00) + (galoes_mistura * 25.00)

print(f"Para comprar apenas latas de 18 litros, você precisará de {latas_18} lata(s), custando R$ {preco_latas_18:.2f}.")
print(f"Para comprar apenas galões de 3,6 litros, você precisará de {galoes_3_6} galão(ões), custando R$ {preco_galoes_3_6:.2f}.")
print(f"Para misturar latas e galões, você precisará de {latas_mistura} lata(s) e {galoes_mistura} galão(ões), custando R$ {preco_mistura:.2f}.")
