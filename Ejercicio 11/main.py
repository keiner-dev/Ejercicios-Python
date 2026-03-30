import os


os.system("clear")

cliente = 0
total_venta = 0

cono = 0
vaso = 0
banana_split = 0

print("Bienvenido a La Heladeria")

while True:
    try:
        print("\nMenu")
        print("1. cono = 3000")
        print("2. vaso = 4000") 
        print("3. banana split = 9000")
        print("4. Salir")
    
        opcion = int(input("Elija el producto: "))
    
        if opcion == 4:
            break
        
        cantidad = int(input("Ingrese la cantidad: "))
        
        if opcion == 1:
            total = cantidad * 3000
            cono += cantidad
        elif opcion == 2:
            total = cantidad * 4000
            vaso += cantidad
        elif opcion == 3:
            total = cantidad * 9000
            banana_split += cantidad  # ← CORREGIDO: era "="
        else:
            print("Opción inválida")
            continue  # ← Salta al siguiente ciclo
        
        # ← ESTO ESTABA MAL INDENTADO
        print("Total a pagar:", total)
        total_venta += total
        cliente += 1
        
    except ValueError:
        print("Opción no válida")
        input("Presione Enter para continuar...")

# Determinar producto más vendido
if cono > vaso and cono > banana_split:
    mas_vendido = "cono"
elif vaso > cono and vaso > banana_split:
    mas_vendido = "vaso"
else:
    mas_vendido = "banana split"  # ← CORREGIDO: misma variable

print("\n-----RESULTADOS FINALES-----")
print("Total vendido:", total_venta)
print("Cantidad de clientes atendidos:", cliente)
print("Producto más vendido:", mas_vendido)
print(f"Conos vendidos: {cono}")
print(f"Vasos vendidos: {vaso}")
print(f"Banana split vendidos: {banana_split}")


