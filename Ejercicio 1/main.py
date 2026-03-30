
print("Bienvenido a la heladeria, ")

vainilla = 0
chocolate = 0
fresa = 0

print("Sabores de helados: Vainilla, chocolate, fresa.")

for i in range(5):
    sabor = input("Ingrese el sabor del helado: ")

    if sabor == "vainilla":
        vainilla += 1
    elif sabor == "chocolate":
        chocolate += 1
    elif sabor == "fresa":
        fresa += 1
    else:
        print("Sabor no valido")

print("Pedidos de vainilla: ",vainilla)
print("Pedidos de chocolate: ",chocolate)
print("Pedido de fresa: ", fresa)