print("""
      =============== PROMOÇÃO DE CARNES ==================
      |                      Até 5 Kg       Acima de 5 Kg |
      | File Duplo     R$ 4,90 por Kg      R$ 5,80 por Kg |
      | Alcatra        R$ 5,90 por Kg      R$ 6,80 por Kg |
      | Picanha        R$ 6,90 por Kg      R$ 7,80 por kg |
      """)

tipo_carne = input("Digite o tipo de carne que deseja (F-File Duplo / A-Alcatra / P-Picanha): ").upper()
quantidade = float(input("Agora informe a quantidade (em Kg): "))

if tipo_carne == 'F':
    if quantidade <= 5:
        preco_kg = 4.90
    else:
        preco_kg = 5.80
    tipo_carne_nome = "File Duplo"
elif tipo_carne == 'A':
    if quantidade <= 5:
        preco_kg = 5.90
    else:
        preco_kg = 6.80
    tipo_carne_nome = "Alcatra"
elif tipo_carne == 'P':
    if quantidade <= 5:
        preco_kg = 6.90
    else:
        preco_kg = 7.80
    tipo_carne_nome = "Picanha"
else:
    print("Tipo de carne inválida!")
    exit()

preco_total = quantidade * preco_kg

forma_pagamento = input("A compra será feito no cartão Tabajara? (S/N): ").upper()

if forma_pagamento == 'S':
    desconto = preco_total * 0.05
else:
    desconto = 0.0
    
valor_a_pagar = preco_total - desconto

print("\n=== CUPOM FISCAL ===")
print(f"Tipo de carne: {tipo_carne_nome}")
print(f"Quantidade de carne: {quantidade:.2f} kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if forma_pagamento == 'S' else 'Outro'}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")