import functions as func
import users 

user = func.authentication()



choice = func.actions(user)


match choice:
    case "3":
        if user == "admin":
            print("\n Todos os usuários e suas senhas: \n")
            for i in users.users:
                print(f"{i}: {users.users[i]["passw"]}")
        else:
            quit()
    case "4":
        quit()
