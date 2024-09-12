pontos = 0

pergunta_1 = input("Telefonou para a vítima? (sim ou não): ").strip().lower()
if pergunta_1 == 'sim':
    pontos += 1

pergunta_2 = input("Esteve no local do crime? (sim ou não): ").strip().lower()
if pergunta_2 == 'sim':
    pontos += 1
    
pergunta_3 = input("Mora perto da vítima? (sim ou não): ").strip().lower()
if pergunta_3 == 'sim':
    pontos += 1

pergunta_4 = input("Devia para a vítima? (sim ou não): ").strip().lower()
if pergunta_4 == 'sim':
    pontos += 1

pergunta_5 = input("Já trabalhou com a vítima? (sim ou não): ").strip().lower()
if pergunta_5 == 'sim':
    pontos += 1


if pontos == 2:
    classificada = "Suspeita"
elif pontos == 3 or pontos == 4:
    classificada = "Cúmplice"
elif pontos == 5:
    classificada = "Assassino"
else:
    classificada = "Inocente"
    
print(f"Classificação: {classificada}")