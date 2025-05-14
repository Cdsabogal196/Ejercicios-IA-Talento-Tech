estudiantes = []

print("Ingresa los datos de los estudiantes:")

while True:
    nombre = input("Nombre del estudiante (o escribe 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break

    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i + 1} de {nombre}: "))
                notas.append(nota)
                break
            except ValueError:
                print("Por favor, ingresa un número válido.")

    promedio = sum(notas) / len(notas)
    estudiantes.append({"nombre": nombre, "notas": notas, "promedio": promedio})

print("\n--- Resultados ---")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Notas: {estudiante['notas']}, Promedio: {estudiante['promedio']:.2f}")