numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000:
    print("Número inválido")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    print(f"{numero} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades")