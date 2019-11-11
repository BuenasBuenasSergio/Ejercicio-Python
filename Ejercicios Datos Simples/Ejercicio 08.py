#Realizando un division introducioendo los datos en inputs, mmuestra el cociente y el reso
dividendo = int(input("Pon dividendo: " ))
divisor = int(input("Pon un divisor: "))
cociente = str(dividendo % divisor)
resultado = str(dividendo / divisor)
print("El resultado es: " + resultado + " y el cociente es " + cociente)