

##us1/ create registro

##lista vacia
users =[[],[]]

def createUser():
    user = []
    id = int(input("ingresa documento de identificacion"))
    user.append(id)
    user_Name = input("ingresa nombre")
    user.append(user_Name)
    user_last_name = input("ingresar apellidos")    
    user.append(user_last_name)
    phone = input("ingresa tu telefono")
    user.append(phone)
    user_email = input("")
    user.append(user_email)
    user_password = input("ingresa contraseña")
    user.append(user_password)
    users.append(user)

createUser()
createUser()

print(users)


