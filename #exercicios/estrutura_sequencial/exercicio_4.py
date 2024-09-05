soma_notas = 0

for i in range(1, 5):
    nota = float(input(f"Digite a {i}ª nota do bimestre: "))
    soma_notas += nota
    
media = soma_notas / 4
print(f"Média: {media:.2f}")