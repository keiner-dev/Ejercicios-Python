import os

os.system("clear")

bajo = 0
medio = 0
alto = 0


for i in range(5):
    name = input("Ingrese su nombre: ")
    day = int(input("Ingrese los dias asistidos a la semana: "))
    time = float(input("Minutos entrenados por dia: "))

    if day < 3:
        print(f"{name}: Bajo compromiso")
        bajo += 1
    elif day <= 4:
        print(f"{name}: Compromiso medio")
        medio += 1
    else:
        print(f"{name}: Compromiso alto")
        alto += 1

print("\n" + "="*40)
print("RESUMEN FINAL")
print("="*40)
print(f"Bajo compromiso:     {bajo} personas")
print(f"Compromiso medio:    {medio} personas")
print(f"Compromiso alto:     {alto} personas")
print(f"Total registrado:    {bajo + medio + alto}")