valor_saque = int(input("Digite o valor do saque (entre 10 e 600 reais): R$ "))

if valor_saque < 10 or valor_saque > 600:
    print("Valor inválido! O valor deve estar entre 10 e 600 reais.")
else:
    notas_100 = valor_saque // 100
    valor_saque %= 100
    
    notas_50 = valor_saque // 50
    valor_saque %= 50
    
    notas_10 = valor_saque // 10
    valor_saque %= 10
    
    notas_5 = valor_saque // 5
    valor_saque %= 5
    
    notas_1 = valor_saque
    
    print("Notas fornecidas:")
    if notas_100 > 0:
        print(f"{notas_100} nota(s) de 100 reais")
    if notas_50 > 0:
        print(f"{notas_50} nota(s) de 50 reais")
    if notas_10 > 0:
        print(f"{notas_10} nota(s) de 10 reais")    
    if notas_5 > 0:
        print(f"{notas_5} nota(s) de 5 reais")
    if notas_1 > 0:
        print(f"{notas_1} nota(s) de 1 reais")    