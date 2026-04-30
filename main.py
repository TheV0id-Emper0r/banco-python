import functions as func
import os
import json

directory = os.path.dirname(os.path.abspath(__file__))
users_path = os.path.join(directory, "users.json")
with open(users_path, "r") as file:
    users = json.load(file)



while True:
    init_choice = func.init()
    match init_choice:
        case "2":
            func.create_user(users, users_path)
        case "1":
            user = func.authentication(users)
            break
        case "3":
            quit()




while True:
    choice = func.actions(user, users)

    match choice:
        case "1":
            func.deposit(user, users, users_path)

        case "2":
            func.withdraw(user, users, users_path)

        case "3":
            if user == "admin":
                print("\n Todos os usuários e suas senhas: \n")
                for i in users:
                    print(f"Usuário: {i} | Senha: {users[i]["passw"]} | Lula Coins: {users[i]["money"]}")
            else:
                quit()

        case "4":
            quit()
