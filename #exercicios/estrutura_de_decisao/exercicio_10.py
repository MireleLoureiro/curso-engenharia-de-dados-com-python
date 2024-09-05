turno_estudo = input("Digite em qual turno você estuda (M-Matutino / V-Vespertino / N-Noturno): ").upper()

if turno_estudo == 'M':
    print("Bom dia!")
elif turno_estudo == 'V':
    print("Boa tarde!")
elif turno_estudo == 'N':
    print("Boa noite!")
else:
    print("Valor inválido!")