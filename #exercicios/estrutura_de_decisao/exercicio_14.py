nota_1 = float(input("Digite a 1ª nota: "))
nota_2 = float(input("Digite a 2ª nota: "))
media = (nota_1 + nota_2) / 2

if 9.0 <= media <= 10.0:
    conceito = 'A'
    status = "APROVADO"
elif 7.5 <= media < 9.0: 
    conceito = 'B'
    status = "APROVADO"
elif 6.0 <= media < 7.5:
    conceito = 'C'
    status = "APROVADO"
elif 4.0 <= media < 6.0:
    conceito = 'D'
    status = "REPROVADO"
else:
    conceito = 'E'
    status = "REPROVADO"
    
print(f"Notas: {nota_1:.2f}, {nota_2:.2f}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")
print(f"Status: {status}")
    