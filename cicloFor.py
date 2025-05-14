txt = input("Ingrese un texto: ")
caracter = input("Ingrese un caracter: ")
contador = txt.lower().count(caracter.lower())

print(f"La cantidad de veces que se repite el '{caracter}' en el texto '{txt}' son {contador} veces")
