dato = input("Ingrese un texto: ")
cantidad = len(dato)
contador = 0
cantidadcaracteres = 0

while contador < cantidad:
    if dato[contador].lower() == 'a':
        cantidadcaracteres += 1 
        print(f"se encontro 'a' en la posicion {contador}") 
    contador += 1  

print(f"La cantidad de veces que se repite la letra 'a' son {cantidadcaracteres}")