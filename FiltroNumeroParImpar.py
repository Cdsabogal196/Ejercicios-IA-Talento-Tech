data = int(input("Ingresa la cantidad de números que vas a ingresar en la lista: "))

lista = []
contador=0
contador2=0
for i in range(data):
    numero = int(input(f"Ingrese el número {i+1}: "))
    lista.append(numero)

for numero in lista:
    if numero % 2 == 0:
        contador=contador+1
    else:
        contador=contador+0
        contador2=contador2+1
        
if contador==len(lista):
    print("Todos los numeros son pares, la cantidad de numeros pares son",contador)
elif contador==0:
    print("Todos los numeros son impares, la cantidad de numeros pares son",contador2)
else:
    print("Hay una mezcla de ambos hay",contador,"pares y",contador2,"impares")

        
    