#Repite el nombre introducido las veces que indiques
#\n es el salto de linea y * int(nveces) indica que se repite la linea 

name = input("Introduce tu nombre: ")
nveces = input("Introduce las veces que se repite")

print((name + "\n") * int(nveces))