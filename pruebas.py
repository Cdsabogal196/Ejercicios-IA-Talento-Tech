#print("Hola mundo")
"""
n1 = 8
n2 = 2
print(n1)
print(n2)
print("la suma de",n1,"y",n2,"es",n1+n2)
print("la resta de",n1,"y",n2,"es",n1-n2)
print("la multiplicacion de",n1,"y",n2,"es",n1*n2)
print("la division de",n1,"y",n2,"es",n1/n2)
n3 = 1000
print("la variable n3 contiene el valor: ",n3)

a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
print("la variable a contiene el valor: ",a)
print("la variable b contiene el valor: ",b)
print("la suma de",a,"y",b,"es",a+b)

nombre = input("ingrese su nombre: ")
edad = input("ingrese su edad: ")
print("hola ",nombre, "tienes ",edad," años")

dato = input("ingrese un dato: ")
print("el dato ingresado es: ",dato)
print("el tipo de dato ingresado es: ",type(dato))
dato = float(dato)
print("el dato ingresado es: ",dato)
print("el tipo de dato ingresado es: ",type(dato))
dato = str(dato)
print("el dato ingresado es: ",dato)
print("el tipo de dato ingresado es: ",type(dato))

print('Carlos "El profe" Fadul')

nombre = "Carlos Fadul es un profe de IA"
print(len(nombre))
#print(nombre[19:])
"""
"""cadena = "el hijo de rana rin rin renacuajo"
cadena=cadena.capitalize()
print(cadena)
cadena=cadena.upper()
print(cadena)"""


texto=input("Ingrese un texto: ")
caracter=input("Ingrese el caracter a buscar: ")


posicion=texto.find(caracter)
cantidad=texto.count(caracter)
print("La letra",caracter,"aparece",cantidad,"veces en el texto")