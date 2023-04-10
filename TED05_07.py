usuarios = []

while True:
    nome = input("Digite o nome do usuário (ou 'sair' para encerrar o programa): ")
    if nome == "sair":
        break
    idade = int(input("Digite a idade do usuário: "))
    email = input("Digite o e-mail do usuário: ")
    usuario = {"nome": nome, "idade": idade, "email": email}

