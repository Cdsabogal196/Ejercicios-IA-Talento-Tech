cadena = input("Ingrese una cadena de caracteres: ")
a = cadena.casefold()
print("Cadena en minúsculas:", a)

ancho = int(input("Ingrese el número total de espacios para centrar la cadena: "))
b = cadena.center(ancho)
print("Cadena centrada:", b)

letra = input("Ingrese la letra que quiere contar: ")
contador = a.count(letra)
print(f"La letra '{letra}' aparece {contador} veces en la cadena.")
