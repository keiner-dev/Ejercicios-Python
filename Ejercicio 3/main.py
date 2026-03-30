print("Bienvenido a la cafetería")

print("Bebidas disponibles:")
print("café = 4000")
print("té = 3500")
print("jugo = 5000")

bebida = input("¿Qué bebida deseas comprar? ")
cantidad = int(input("¿Cuántas unidades deseas? "))

if bebida == "café":
    total = 4000 * cantidad
elif bebida == "té":
    total = 3500 * cantidad
elif bebida == "jugo":
    total = 5000 * cantidad
else:
    print("Bebida no disponible")
    total = 0

print("Total a pagar:", total)