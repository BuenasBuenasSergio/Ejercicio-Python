name = input("Como te llamas: ")
gender = input("Eres hombre o mujer(H o M) ")
if gender == "M":
    if name.lower() < "m":
        print("Estas en el frupo A")
    else:
        print("Estas en grupo B")
else:
    if name.lower() < "n":
        print("Estas en el grupo A")
    else:
        print("Estas el grupo B")