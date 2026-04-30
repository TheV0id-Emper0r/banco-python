import json


def init():
    print("\n"*5, "-"*25, "Lula Bank", "-"*25)
    print(" Deseja fazer login, ou criar um usuário? \n 1. Fazer login \n 2. Criar novo usuário \n 3. Sair")
    while True:
        init_choice = input("Digite o número da escolha: ")
        if init_choice in ["1", "2", "3"]:
            return init_choice
        else:
            print("Escolha inválida! Tente novamente.")

def create_user(users, users_path):
    print("\n"*5, "-"*25, "NOVO USUÁRIO", "-"*25)
    while True:
        new_name = input("\n Insira o nome do seu novo usuário: ").lower()
        if new_name not in users:
            break
        else:
            print("\n Este usuário já existe, tente outro nome.")

    while True:
        new_passw = input("\n Insira sua nova senha: ")
        confirm_passw = input(" Confirme a nova senha: ")

        if new_passw == confirm_passw:
            users[new_name] ={
                "passw": new_passw,
                "money": 0.0
            }
            save_json(users, users_path)
            print("\n Usuário cadastrado com sucesso no Lula Bank!")
            break
        else:
            print(" Senha incorreta! Tente novamente.")

def authentication(users):
    print("\n"*5, "-"*25, "AUTENTICAÇÃO", "-"*25)
    aut = True
    while aut == True:
                # VERIFICAR USUÁRIO
        while True:
            tryuser = input("\n Insira seu usuário: ").lower()
            if tryuser not in users:
                print("\n Usuário inválido! Tente novamente.\n")
            else: 
                break

                # VERIFICAR SENHA
        trypassw = input("\n Insira a senha: ")
        if trypassw == users[tryuser]["passw"]:
            aut = False
        else:
            print("\n Senha incorreta! Tente novamente.")

    print(f"\n         Hello, {tryuser.capitalize()}\n")
    return tryuser 

def actions(user, users):
    print("\n"*2, "-"*25, "AÇÕES", "-"*25)
    print(f"\n Seu saldo atual é: {users[user]["money"]} Lula Coins")

        # ADMIN SECTION
    if user == "admin":
        print("""
 1. Depositar Lula Coins \n 
 2. Sacar Lula Coins \n 
 3. Ver todos os usuários, suas senhas e seus Lula Coins \n
 4. Sair""")
        while True:
            choice = input("\n Selecione digitando o número: ")
            if choice in ["1", "2", "3", "4"]:
                return choice
            else:
                print("\n Escolha inválida!")

        # USER SECTION
    else:
        print("""
 1. Depositar Lula Coins \n 
 2. Sacar Lula Coins \n 
 3. Sair""")
        while True:
            choice = input("\n Selecione digitando o número: ")
            if choice in ["1", "2", "3"]:
                return choice
            else:
                print("\n Escolha inválida!")

def deposit(user, users, users_path):
    print("\n"*5, "-"*25, "DEPOSITAR", "-"*25)
    while True:
        try:
            newmoney = float(input("\n Insira o valor de Lula Coins a ser depositado: "))
            if newmoney >= 0:
                print(f"\n Parabéns, {newmoney} Lula Coins foram depositados na sua conta!")
                break
        except:
            print("Apenas números positivos são aceitos!")
    users[user]["money"] += newmoney
    save_json(users, users_path)


def withdraw(user, users, users_path):
    print("\n"*5, "-"*25, "SACAR", "-"*25)
    while True:
        try:
            newmoney = float(input("\n Insira o valor de Lula Coins a ser sacado: "))
            if newmoney >= 0:
                break
        except:
            print("\n Apenas números positivos são aceitos!")

    if users[user]["money"] - newmoney >= 0:
        users[user]["money"] -= newmoney
        save_json(users, users_path)
    else:
        print("\n Lula Coins insuficientes!")
            

def save_json(users, users_path):
    with open(users_path, "w") as file:
        json.dump(users, file, indent=4)

