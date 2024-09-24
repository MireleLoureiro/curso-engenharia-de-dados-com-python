print("""
      ================ TABELA DE PREÇOS ================
      |                   Até 5 Kg       Acima de 5 Kg |
      | Morango     R$ 2,50 por Kg      R$ 2,20 por Kg |
      | Maça        R$ 1,80 por Kg      R$ 1,50 por Kg |
      """)

morangos_kg = float(input("Informe a quantidade (em Kg) de morangos: "))
macas_kg = float(input("Informe a quantidade (em Kg) de maças: "))

if morangos_kg <= 5.0:
    preco_morangos = 2.50 * morangos_kg
else:
    preco_morangos = 2.20 * morangos_kg

if macas_kg  <= 5.0:
    preco_macas = 1.80 * macas_kg
else:
    preco_macas = 1.50 * macas_kg
    
preco_total = preco_morangos + preco_macas

if (morangos_kg + macas_kg > 8) or (preco_total > 25):
    preco_total = preco_total - (0.1 * preco_total)

print(f"Valor a ser pago: R$ {preco_total:.2f}")