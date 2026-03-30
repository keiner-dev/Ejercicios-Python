print("Bienvenido a la academia")

while True:
    asistencias = int(input("Ingresa la cantidad de clases asistidas: "))
    try:
        if asistencias < 5:
            print("asistencias baja")

        elif 5 <= asistencias <= 8:
            print("asistencia media")

        else:
            print("asistencia alta")
    except ValueError:
        print("ingrese valores correctos")