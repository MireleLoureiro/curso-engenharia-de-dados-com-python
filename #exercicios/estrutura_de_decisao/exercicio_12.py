valor_hora = float(input("Digite o valor da sua hora: R$ "))
quantidade_horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * quantidade_horas

if salario_bruto <= 900.0:
    desconto = 0
elif salario_bruto <= 1500.0:
    desconto = 5
elif salario_bruto <= 2500.0:
    desconto = 10
else:
    desconto = 20

imposto_renda = salario_bruto * (desconto / 100)
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11
descontos = imposto_renda + sindicato
salario_liquido = salario_bruto - descontos

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"IR ({desconto}%): R$ {imposto_renda:.2f}")
print(f"Sindicato (3%): R$ {sindicato:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}") 
print(f"Total de descontos: R$ {descontos:.2f}")
print(f"Salário Liquido: R$ {salario_liquido:.2f}")