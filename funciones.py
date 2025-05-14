"""def mifuncion(a,b):
    print("Hola amigos")
    print(a+b)

for i in range(1, 11):
    mifuncion(5,8)

def resta(a,b):
    return a-b
print(resta(9,6))
"""

def calculadora(a,b,operador):
    if operador=="+":
        return "El resultado de la suma es",a+b
    if operador=="-":
        return "El resultado de la resta es",a-b
    if operador=="/":
        return "El resultado de la division es",a/b
    if operador=="*":
        return "El resultado de la multiplicacion es",a*b

operador = input("Ingresa + para sumar, - para restar, / para dividir y * para multiplicar: ")
numero1 = float(input("Ingresa el primer número para realizar la operación: "))
numero2 = float(input("Ingresa el segundo número para realizar la operación: "))
print(calculadora(numero1,numero2,operador))