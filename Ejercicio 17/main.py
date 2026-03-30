total_dia = 0

# Contadores por servicio
corte = 0
cepillado = 0
tintura = 0

# Registrar 7 clientes
for i in range(1, 8):
    print(f"\nCliente #{i}")
    
    nombre = input("Nombre: ")
    servicio = input("Servicio (corte/cepillado/tintura): ").lower()
    valor = float(input("Valor pagado: "))

    # Acumular dinero
    total_dia += valor

    # Contar servicios
    if servicio == "corte":
        corte += 1
    elif servicio == "cepillado":
        cepillado += 1
    elif servicio == "tintura":
        tintura += 1
    else:
        print("Servicio no válido")

# Mostrar resultados
print("\n--- RESULTADOS ---")
print(f"Total del día: {total_dia}")
print(f"Cortes: {corte}")
print(f"Cepillados: {cepillado}")
print(f"Tinturas: {tintura}")

# Determinar servicio más solicitado
mayor = corte
servicio_mas = "corte"

if cepillado > mayor:
    mayor = cepillado
    servicio_mas = "cepillado"

if tintura > mayor:
    mayor = tintura
    servicio_mas = "tintura"

print(f"Servicio más solicitado: {servicio_mas}")