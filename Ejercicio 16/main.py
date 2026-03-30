# Acumuladores por categoría
alimento_total = 0
juguete_total = 0
accesorio_total = 0

# Registrar 10 ventas
for i in range(1, 11):
    print(f"\nVenta #{i}")
    
    categoria = input("Categoría (alimento/juguete/accesorio): ").lower()
    valor = float(input("Valor de la compra: "))

    # Acumular según categoría
    if categoria == "alimento":
        alimento_total += valor
    elif categoria == "juguete":
        juguete_total += valor
    elif categoria == "accesorio":
        accesorio_total += valor
    else:
        print("Categoría no válida")

# Mostrar totales
print("\n--- RESULTADOS ---")
print(f"Total en alimento: {alimento_total}")
print(f"Total en juguete: {juguete_total}")
print(f"Total en accesorio: {accesorio_total}")

# Determinar cuál generó más dinero
mayor = alimento_total
categoria_mayor = "alimento"

if juguete_total > mayor:
    mayor = juguete_total
    categoria_mayor = "juguete"

if accesorio_total > mayor:
    mayor = accesorio_total
    categoria_mayor = "accesorio"

print(f"La categoría que generó más dinero fue: {categoria_mayor} con {mayor}")