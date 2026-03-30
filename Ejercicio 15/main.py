total_recaudado = 0
carros = 0
motos = 0

mayor_pago = 0
vehiculo_mayor = ""

# Registrar 8 vehículos
for i in range(1, 9):
    print(f"\nVehículo #{i}")
    
    placa = input("Ingrese la placa: ")
    tipo = input("Tipo (carro/moto): ").lower()
    horas = int(input("Horas parqueado: "))

    # Calcular pago
    if tipo == "carro":
        pago = horas * 4000
        carros += 1
    elif tipo == "moto":
        pago = horas * 2000
        motos += 1
    else:
        print("Tipo no válido, se tomará como moto")
        pago = horas * 2000
        motos += 1

    print(f"Pago del vehículo: {pago}")

    # Acumular total
    total_recaudado += pago

    # Verificar el mayor pago
    if pago > mayor_pago:
        mayor_pago = pago
        vehiculo_mayor = placa

# Resultados
print("\n--- RESULTADOS ---")
print(f"Total recaudado: {total_recaudado}")
print(f"Cantidad de carros: {carros}")
print(f"Cantidad de motos: {motos}")
print(f"Vehículo que más pagó: {vehiculo_mayor} con {mayor_pago}")