"""
frutas = ("manzana", "banana", "naranja", "kiwi", "mango")

print(len(frutas))
print(frutas[2])
print(frutas[1:3])
print(frutas.count("manzana"))
print(frutas.index("kiwi"))

frutas_lista = list(frutas)
frutas_lista.insert(0, "fresa")
print(frutas_lista)
"""
frutas = {"manzana", "banana", "naranja", "kiwi", "mango"}
frutas2 = {"banana", "naranja", "kiwi"}

print(frutas.issuperset(frutas2))         
print(frutas.issuperset(frutas2))
print(frutas.union(frutas2))
print(frutas.intersection(frutas2))
