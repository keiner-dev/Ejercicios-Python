total_recaudado = 0

# Contadores por plan
basico = 0
premium = 0
familiar = 0

# Cantidad de personas a registrar
n = int(input("¿Cuántas personas desea registrar?: "))

for i in range(1, n + 1):
    print(f"\nPersona #{i}")
    
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    plan = input("Tipo de plan (basico/premium/familiar): ").lower()

    # Validaciones por edad
    if edad < 18:
        print("Registro juvenil")
    elif edad >= 60:
        print("Beneficio senior")

    # Asignar valor según plan
    if plan == "basico":
        total_recaudado += 50000
        basico += 1
    elif plan == "premium":
        total_recaudado += 90000
        premium += 1
    elif plan == "familiar":
        total_recaudado += 130000
        familiar += 1
    else:
        print("Plan no válido")

# Resultados
print("\n--- RESULTADOS ---")
print(f"Total recaudado: {total_recaudado}")
print(f"Básico: {basico}")
print(f"Premium: {premium}")
print(f"Familiar: {familiar}")

# Determinar plan más vendido
mayor = basico
plan_mas = "basico"

if premium > mayor:
    mayor = premium
    plan_mas = "premium"

if familiar > mayor:
    mayor = familiar
    plan_mas = "familiar"

print(f"Plan más vendido: {plan_mas}")