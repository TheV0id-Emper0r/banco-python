import json


def init():
    print(" Deseja fazer login, ou criar um usuário? \n 1. Fazer login \n 2. Criar novo usuário \n 3. Sair")
    while True:
        init_choice = input("Digite o número da escolha: ")
        if init_choice in ["1", "2", "3"]:
            return init_choice
        else:
            print("Escolha inválida! Tente novamente.")

def create_user(users, users_path):
    while True:
        new_name = input("Insira seu novo nome: ").lower()
        if new_name not in users:
            break
        else:
            print("Este usuário já existe, tente outro nome.")

    while True:
        new_passw = input("Insira sua nova senha: ")
        confirm_passw = input("Confirme a nova senha: ")

        if new_passw == confirm_passw:
            users[new_name] ={
                "passw": new_passw,
                "money": 0.0
            }
            save_json(users, users_path)
            print("Usuário cadastrado com sucesso!")
            break
        else:
            print("Senha incorreta! Tente novamente.")

def authentication(users):
    aut = True
    while aut == True:
                # VERIFICAR USUÁRIO
        while True:
            print("\n"*2, "-"*25, "AUTENTICAÇÃO", "-"*25)
            tryuser = input("Insira seu nome: ").lower()
            if tryuser not in users:
                print("Usuário inválido! Tente novamente.\n")
            else: 
                break

                # VERIFICAR SENHA
        while True:
            trypassw = input("insira a senha: ")
            if trypassw == users[tryuser]["passw"]:
                aut = False
                break
            else:
                print("Senha incorreta! Tente novamente.\n")
                break
    print(f"\n Hello, {tryuser.capitalize()}\n")
    return tryuser 

def actions(user, users):
    print("\n"*2, "-"*25, "AÇÕES", "-"*25)
    print(f"Seu saldo atual é: {users[user]["money"]}")

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

def deposit(user, users, users_path):
    while True:
        try:
            newmoney = float(input("Insira o valor a ser depositado: "))
            newmoney > 0
            break
        except:
            print("Apenas números positivos são aceitos!")

    users[user]["money"] += newmoney
    save_json(users, users_path)


def withdraw(user, users, users_path):
    while True:
        try:
            newmoney = float(input("Insira o valor a ser sacado: "))
            newmoney > 0
            break
        except:
            print("Apenas números positivos são aceitos!")


    if users[user]["money"] - newmoney >= 0:

        users[user]["money"] -= newmoney
        save_json(users, users_path)

    else:
        print("Saldo insuficiente!")
            

def save_json(users, users_path):
    with open(users_path, "w") as file:
        json.dump(users, file, indent=4)

