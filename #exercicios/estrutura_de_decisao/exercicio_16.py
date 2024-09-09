import math

valor_a = float(input("Digite o valor de A: "))

if valor_a == 0:
    print("A equação não é do 2º grau.")
else:
    valor_b = float(input("Digite o valor de B: "))
    valor_c = float(input("Digite o valor de C: "))
    delta = math.pow(valor_b, 2) - (4 * valor_a * valor_c)
    
    if delta < 0:
        print("A equação não possui raizes reais")
    elif delta == 0:
        raiz = - (valor_b + math.sqrt(delta)) / (2 * valor_a)
        print(f"A equação possui apenas uma raiz real: {raiz:.1f}")
    else:
        raiz_1 = (- valor_b + math.sqrt(delta)) / (2 * valor_a)
        raiz_2 = (- valor_b - math.sqrt(delta)) / (2 * valor_a)
        print(f"A equação possui duas raiz reais: {raiz_1:.1f} e {raiz_2:.1f}")