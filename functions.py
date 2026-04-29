import users
def authentication():
    aut = True
    while aut == True:
                # VERIFICAR USUÁRIO
        while True:
            print("\n"*2, "-"*25, "AUTENTICAÇÃO", "-"*25)
            tryuser = input("Insira seu nome: ").lower()
            if tryuser not in users.users:
                print("Usuário inválido! Tente novamente.\n")
            else: 
                break

                # VERIFICAR SENHA
        while True:
            trypassw = input("insira a senha: ")
            if trypassw == users.users[tryuser]["passw"]:
                aut = False
                break
            else:
                print("Senha incorreta! Tente novamente.\n")
                break
    print(f"\n Hello, {tryuser.capitalize()}\n")
    return tryuser 

def actions(user):
    print("\n"*2, "-"*25, "AÇÕES", "-"*25)
    print(f"Seu saldo atual é: {users.users[user]["money"]}")

        # ADMIN SECTION
    if user == "admin":
        print("""
 1. Depositar dinheiro \n 
 2. Sacar dinheiro \n 
 3. Ver todos os usuários e suas senhas \n
 4. Sair""")
        while True:
            choice = input("\n Selecione digitando o número: ")
            if choice in ["1", "2", "3", "4"]:
                return choice
            else:
                print("Escolha inválida!")

        # USER SECTION
    else:
        print("""
 1. Depositar dinheiro \n 
 2. Sacar dinheiro \n 
 3. Sair""")
        while True:
            choice = input("\n Selecione digitando o número: ")
            if choice in ["1", "2", "3"]:
                return choice
            else:
                print("Escolha inválida!")





