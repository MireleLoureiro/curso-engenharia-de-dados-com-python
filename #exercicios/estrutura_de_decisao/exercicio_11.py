salario = float(input("Digite seu salário: R$ "))

if salario <= 280.0:
    percentual = 20
elif salario <= 700.0:
    percentual = 15
elif salario <= 1500.0:
    percentual = 10
else:
    percentual = 5

valor_aumento = salario * (percentual / 100)
novo_salario = salario + valor_aumento
    
print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")