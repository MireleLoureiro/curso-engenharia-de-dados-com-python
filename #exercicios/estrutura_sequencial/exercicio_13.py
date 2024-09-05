altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M/F): ").upper()

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None
    print("Opção inválida.")

if peso_ideal is not None:    
    print(f"Seu peso ideal = {peso_ideal:.2f} Kg")