# Precios de productos
precios = {
    "cafe": 4000,
    "capuchino": 7000,
    "pastel": 6000
}

total_dia = 0  # acumulado del día

while True:
    print("\n--- Nueva compra ---")
    total_cliente = 0

    while True:
        print("\nMenú:")
        print("cafe = 4000")
        print("capuchino = 7000")
        print("pastel = 6000")
        print("Escribe 'fin' para terminar la compra")

        producto = input("Seleccione producto: ").lower()

        if producto == "fin":
            break

        if producto in precios:
            total_cliente += precios[producto]
            print(f"Agregado {producto}. Subtotal: {total_cliente}")
        else:
            print("Producto no válido")

    # Aplicar descuento
    if total_cliente > 20000:
        descuento = total_cliente * 0.10
        total_cliente -= descuento
        print(f"Se aplicó descuento del 10%: -{descuento}")

    print(f"Total a pagar por cliente: {total_cliente}")
    total_dia += total_cliente

    salir = input("\n¿Desea registrar otro cliente? (si/salir): ").lower()
    if salir == "salir":
        break

print("\n--- Cierre del día ---")
print(f"Total acumulado del día: {total_dia}")