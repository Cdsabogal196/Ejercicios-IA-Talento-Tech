estudiantes =[]
calificaciones =[]

def agregar_estudiante(nombre,calificaciones):
    estudiante={
        'nombre': nombre,
        'calificaciones':calificaciones
    }
    estudiantes.append(estudiante)

def calcular_promedio(nombre):
    for estudiante in estudiantes:
        if estudiante['nombre']==nombre:
            lista= estudiante['calificaciones']
            return sum(lista) / 3
    return None


def mostrar_estudiantes():

    for estudiante in estudiantes:
        nombre=estudiante['nombre']
        calificaciones=estudiante['califiaciones']
        promedio=calcular_promedio(nombre)
        if promedio>=3.0:
         aprobado="Aprobado"
        else:
         aprobado="Reprobado"   
        print(f"Nombre: {nombre}, Calificaciones:{calificaciones}, Promedio:{promedio} estatus:{aprobado}")
def menu():
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Calcular promedio")
    print("4. Salir")
    opcion= input("Selecciona una opción: ")
    return opcion
def main():
    while True:
        opcion=menu()
        if opcion=="1":
            nombre=input("Ingresa el nombre del estudiante: ")
            calificaciones=[]
            for i in range(3):
                calificacion=float(input(f"Ingrese la calificación {i+1}: "))
                calificaciones.append(calificacion)
            agregar_estudiante(nombre,calificaciones)
        elif opcion=="2":
            mostrar_estudiantes()
        elif opcion=="3":
            nombre=input("Ingresa el nombre del estudiante: ")
            promedio=calcular_promedio(nombre)
            if promedio is not None:
                print(f"El promedio de {nombre} es: {promedio}")
            else:
                print("Estudiante no encontrado")
        elif opcion=="4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

main()