
print("Bienvenido")

edad = int(input("Ingrese su edad: "))

if edad < 12:
    precio = 8000
elif edad <= 59:
    precio = 12000
else:
    precio = 9000

print("El precio de la entrada es:", precio)