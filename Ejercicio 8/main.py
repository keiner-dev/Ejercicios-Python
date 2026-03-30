contador = 0

for i in range(6):
    precio = int(input("Ingrese el precio del producto: "))

    if precio > 100000:
        contador += 1

print("Cantidad de productos que cuestan más de 100000:", contador)