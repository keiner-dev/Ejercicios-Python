# Pedir capacidad de la sala
capacidad = int(input("Ingrese la capacidad total de la sala: "))

total_personas = 0
ninos = 0
adultos = 0
adultos_mayores = 0

# Ciclo controlado por la capacidad
while total_personas < capacidad:
    print(f"\nPersona #{total_personas + 1}")
    
    edad = int(input("Ingrese la edad: "))

    # Clasificación
    if edad < 18:
        ninos += 1
        print("Clasificación: Niño")
    elif edad < 60:
        adultos += 1
        print("Clasificación: Adulto")
    else:
        adultos_mayores += 1
        print("Clasificación: Adulto mayor")

    total_personas += 1

    # Preguntar si desean seguir ingresando personas
    continuar = input("¿Desea ingresar otra persona? (si/no): ").lower()
    if continuar == "no":
        break

# Resultados
print("\n--- RESULTADOS ---")
print(f"Total de personas ingresadas: {total_personas}")
print(f"Niños: {ninos}")
print(f"Adultos: {adultos}")
print(f"Adultos mayores: {adultos_mayores}")

# Verificar si se llenó la sala
if total_personas == capacidad:
    print("La sala se llenó")
else:
    print("La sala NO se llenó")