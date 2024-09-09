data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = map(int, data.split('/'))
bissexto = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

if mes < 1 or mes > 12:
    print("Data inválida")
else:
    if dia < 1:
        print("Data inválida")
    elif mes in [1, 3, 5, 7, 8, 10, 12] and dia <= 31:
        print("Data válida")
    elif mes in [4, 6, 9, 11] and dia <= 30:
        print("Data válida")
    elif mes == 2:
        if bissexto and dia <= 29:
            print("Data válida")
        elif not bissexto and dia <= 28:
            print("Data válida")
        else:
            print("Data inválida")
    else:
        print("Data inválida")