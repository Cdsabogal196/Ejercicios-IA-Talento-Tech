estudiantes = {}

def agregar_estudiante(nombre, calificaciones):
    """Agrega un estudiante con sus calificaciones al diccionario."""
    estudiantes[nombre] = calificaciones
    print(f"Estudiante {nombre} agregado con calificaciones: {calificaciones}")

def calcular_promedio(nombre):
    """Calcula el promedio de calificaciones de un estudiante."""
    if nombre in estudiantes:
        calificaciones = estudiantes[nombre]
        promedio = sum(calificaciones) / len(calificaciones)
        return promedio
    else:
        print("Estudiante no encontrado.")
        return None

def mostrar_estado(nombre):
    """Muestra el estado del estudiante (Aprobado o Reprobado)."""
    promedio = calcular_promedio(nombre)
    if promedio is not None:
        estado = "Aprobado" if promedio >= 6 else "Reprobado"
        print(f"El estudiante {nombre} tiene un promedio de {promedio:.2f} y está {estado}.")

def listar_estudiantes():
    """Lista todos los estudiantes con sus promedios y estados."""
    if estudiantes:
        for nombre, calificaciones in estudiantes.items():
            promedio = calcular_promedio(nombre)
            estado = "Aprobado" if promedio >= 6 else "Reprobado"
            print(f"Nombre: {nombre}, Calificaciones: {calificaciones}, Promedio: {promedio:.2f}, Estado: {estado}")
    else:
        print("No hay estudiantes registrados.")

def menu():
    """Muestra el menú de opciones y gestiona la interacción con el usuario."""
    while True:
        print("\n--- Sistema de Gestión de Estudiantes ---")
        print("1. Agregar estudiante")
        print("2. Calcular promedio de un estudiante")
        print("3. Mostrar estado de un estudiante")
        print("4. Listar todos los estudiantes")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del estudiante: ")
            calificaciones = []
            while True:
                try:
                    calificacion = float(input("Ingresa una calificación (o -1 para terminar): "))
                    if calificacion == -1:
                        break
                    calificaciones.append(calificacion)
                except ValueError:
                    print("Por favor, ingresa un número válido.")
            agregar_estudiante(nombre, calificaciones)
        elif opcion == "2":
            nombre = input("Ingresa el nombre del estudiante: ")
            promedio = calcular_promedio(nombre)
            if promedio is not None:
                print(f"El promedio de {nombre} es: {promedio:.2f}")
        elif opcion == "3":
            nombre = input("Ingresa el nombre del estudiante: ")
            mostrar_estado(nombre)
        elif opcion == "4":
            listar_estudiantes()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()