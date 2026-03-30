total_estudiantes = 0
suma_promedios = 0

# Contadores por nivel
bajo = 0
medio = 0
alto = 0

# Para el mejor estudiante
mejor_promedio = 0
mejor_estudiante = ""

# Cantidad de estudiantes (puedes cambiarla)
n = int(input("¿Cuántos estudiantes desea registrar?: "))

for i in range(1, n + 1):
    print(f"\nEstudiante #{i}")
    
    nombre = input("Nombre: ")
    speaking = float(input("Nota speaking: "))
    listening = float(input("Nota listening: "))
    reading = float(input("Nota reading: "))

    # Calcular promedio
    promedio = (speaking + listening + reading) / 3
    print(f"Promedio: {promedio}")

    # Acumular promedios
    suma_promedios += promedio
    total_estudiantes += 1

    # Clasificación
    if promedio < 60:
        bajo += 1
        print("Nivel: Bajo")
    elif promedio < 80:
        medio += 1
        print("Nivel: Medio")
    else:
        alto += 1
        print("Nivel: Alto")

    # Mejor estudiante
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre

# Resultados finales
promedio_general = suma_promedios / total_estudiantes

print("\n--- RESULTADOS ---")
print(f"Promedio general del grupo: {promedio_general}")
print(f"Mejor estudiante: {mejor_estudiante} con {mejor_promedio}")
print(f"Bajo: {bajo}")
print(f"Medio: {medio}")
print(f"Alto: {alto}")