lado_1 = float(input("Digite o 1º lado do triângulo: "))
lado_2 = float(input("Digite o 2º lado do triângulo: "))
lado_3 = float(input("Digite o 3º lado do triângulo: "))

if (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1):
    if lado_1 == lado_2 == lado_3:
        print("Triângulo Equilátero")
    elif (lado_1 == lado_2) or (lado_1 == lado_3) or (lado_2 == lado_3):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores não formam um triângulo")