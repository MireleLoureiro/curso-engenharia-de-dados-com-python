nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Valor inváido! A nota deve estar entre 0 e 10.")
    nota = float(input("Digite uma nota entre 0 e 10: "))

print(f"Nota válida registrada: {nota}")