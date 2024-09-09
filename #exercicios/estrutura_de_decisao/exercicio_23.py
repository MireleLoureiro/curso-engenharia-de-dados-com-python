numero = float(input("Digite um número: "))

if numero == round(numero):
    print(f"{int(numero)} é um número inteiro!")
else:
    print(f"{numero} é um número decimal!")