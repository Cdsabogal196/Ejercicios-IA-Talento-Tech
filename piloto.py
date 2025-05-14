def mostrar_tablas_multiplicar():
    """Muestra las tablas de multiplicar del 1 al 10."""
    for i in range(1, 11):
        print(f"Tabla del {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print("-" * 20)

if __name__ == "__main__":
    mostrar_tablas_multiplicar()