numeros = []
print("Ingresa 10 números:")

for i in range(10):
    while True:
        try:
            numero = float(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

promedio = sum(numeros) / len(numeros)
print(f"Los números ingresados son: {numeros}")
print(f"El promedio de los números es: {promedio:.2f}")