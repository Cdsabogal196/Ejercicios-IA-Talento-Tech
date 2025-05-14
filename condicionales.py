edad = int(input("Ingresa la edad de la persona: "))

if edad < 6:
    print("Primera infancia")
elif edad<13 and edad >=6:
    print("Infancia")
elif edad>=13 and edad<18:
    print("Adolescencia")
elif edad >= 18:
    print("Adulto")
else:
    print("Edad no válida")  