agotados = 0
stock_bajo = 0
stock_normal = 0

# Registrar 10 productos
for i in range(1, 11):
    print(f"\nProducto #{i}")
    
    nombre = input("Nombre del producto: ")
    cantidad = int(input("Cantidad disponible: "))

    # Clasificación
    if cantidad == 0:
        agotados += 1
        print("Estado: Agotado")
    elif cantidad <= 5:
        stock_bajo += 1
        print("Estado: Stock bajo")
    else:
        stock_normal += 1
        print("Estado: Stock normal")

# Resultados
print("\n--- RESULTADOS ---")
print(f"Productos agotados: {agotados}")
print(f"Productos con stock bajo: {stock_bajo}")
print(f"Productos con stock normal: {stock_normal}")