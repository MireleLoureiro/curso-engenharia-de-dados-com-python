letra = input("Digite uma letra: ").lower()

vogais = "aeiou"

if letra in vogais:
    print(f"A letra {letra} é uma vogal")
elif letra.isalpha():
    print(f"A letra {letra} é uma consoante")
else:
    print("Entrada inválida. Por favor digite uma letra.")