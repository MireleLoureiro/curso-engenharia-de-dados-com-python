peso = float(input("Digite o peso de peixes (kg): "))
limite = 50.0
multa_por_quilo = 4.0

if peso > limite:
    excesso = peso - limite
    multa = multa_por_quilo * excesso
else:
    excesso = 0.0
    multa = 0.0

print(f"Peso dos peixes: {peso} kg")
print(f"Excesso de peso: {excesso} kg")
print(f"Multa a pagar: R$ {multa:.2f}")