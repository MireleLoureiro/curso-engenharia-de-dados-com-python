numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite mais um número: "))

operacao = input("Digite qual operação deseja realizar (+, -, *, /): ")
if operacao == '+':
    resultado = numero_1 + numero_2
elif operacao == '-':
    resultado = numero_1 - numero_2
elif operacao == '*':
    resultado = numero_1 * numero_2
elif operacao == '/':
    if numero_2 != 0:
        resultado = numero_1 / numero_2
    else:
        resultado = None
        print("Divisão por zero não é permitida")
else:
    resultado = None
    print("Operação inválida")

if resultado is not None:
    if resultado % 2 == 0:
        paridade = "par"
    else:
        paridade = "ímpar"
    
    if resultado > 0:
        sinal = "positivo"
    else:
        sinal = "negativo"
        
    if resultado == round(resultado):
        tipo = "inteiro"
    else:
        tipo = "decimal"
    
    print(f"Resultado: {resultado}")
    print(f"O número é {paridade}, {sinal} e {tipo}")