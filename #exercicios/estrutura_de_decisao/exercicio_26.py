print("""
    ================ TABELA DE DESCONTOS ===============
    |   Álcool:                                        |
    |   - até 20 litros, desconto de 3% por litro      |
    |   - acima de 20 litros, desconto de 5% por litro |
    |   Gasolina:                                      |
    |   - até 20 litros, desconto de 4% por litro      |
    |   - acima de 20 litros, desconto de 6% por litro |
""")

litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível escolhido (A-álcool, G-gasolina): ").strip().upper()


if tipo_combustivel == 'A':
    valor_litro = litros_vendidos * 1.90
    if litros_vendidos <= 20.0:
        valor_a_pagar = valor_litro - (valor_litro * 0.03)
    else:
        valor_a_pagar = valor_litro - (valor_litro * 0.05)
elif tipo_combustivel == 'G':
    valor_litro = litros_vendidos * 2.50
    if litros_vendidos <= 20.0:
        valor_a_pagar = valor_litro - (valor_litro * 0.04)
    else:
        valor_a_pagar = valor_litro - (valor_litro * 0.06)   
else:
    print("Tipo de combustível inválido.")
    valor_a_pagar = 0.0

print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")