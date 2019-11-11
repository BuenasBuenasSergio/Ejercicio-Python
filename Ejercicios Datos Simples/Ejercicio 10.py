#Simula un creacion de de una contraseña y su verificacion
key = input("Introduce la contraseña: " )
password = input("Repite la contraseña: ")
if key == password.lower():
    print("Contraseña correcta.")
else:
    print("Contaseña errónea.")