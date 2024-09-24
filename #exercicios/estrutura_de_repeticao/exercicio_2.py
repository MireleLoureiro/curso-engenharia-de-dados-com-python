nome = input("Digite seu nome: ").upper()
senha = input("Digite sua senha: ").upper()

while senha == nome:
    print("Erro! A senha não pode ser igual ao nome do usuário!")
    senha = input("Digite sua senha novamente: ").upper()
    
print("Usuário e senha cadastradis com sucesso!")