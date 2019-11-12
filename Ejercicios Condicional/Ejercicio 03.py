#Pequeño contol para saber si las divisiones son validadas en caso de que no lo sean mostrara un mensaje de error
dividendo = int(input("Introduce un dividendo: "))
divisor = int(input("Introduce un divisor"))

if divisor == 0 or dividendo == 0:
    print("Error division no valida")
else:
    print(dividendo/divisor)