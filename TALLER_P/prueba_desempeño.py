#PROYECTO PRUEBA DE DESEMPEÑO: SISTEMA DE GESTION DE ESTUDIANTES.

#CREACION DEL DICCIONARIO:

estudiantes = { 1: {"ID": 1002163511,
                    "Nombre": "Sebastian",
                    "Edad": 15,
                    "Curso": "Noveno",
                    "Estado": "Activo"},

                2: {"ID": 1004150611,
                    "Nombre": "Estefani",
                    "Edad": 14,
                    "Curso": "",
                    "Estado": "Inactivo"},

                3: {"ID": 1043570933,
                    "Nombre": "Angelica",
                    "Edad": 17,
                    "Curso": "Once",
                    "Estado": "Activo"}
}


#FUNCION PARA REGISTRO DE NUEVO ESTUDIANTE  

def registro_de_estudiantes():
        
        if opcion == "1":
            id_estudiante = int(input("Ingrese el No° de documento: "))
            nombre = input("Ingrese el nombre:  ")
            edad = int(input("Ingresa la edad: "))
            curso = input("Ingrese el grado")
            
            id_estudiante = max (estudiantes.keys()) + 1
            
            estudiantes[4] = {
                "id": id_estudiante,
                "Nombre": nombre,
                "Edad": edad,
                "Curso": curso,
                "Estado": "Activo"}
            
            print(f"Estudiantes {id_estudiante}, {nombre}, {edad}, {curso}, ESTUDIANTE AGREGADO CON EXITO")


#FUNCION PARA BUSCAR ESTUDIANTE CON EL METODO GET

def buscar_estudiante(): 
        

        if opcion == "2":
            
            id_estudiante = int(input("Ingrese el Id del estudiante: "))
            id_estudiante = None

            print("Buscando por Id del estudiante ")
            print("Buscando con metodo get")
            print(estudiantes.get(1, "NO ENCONTRADO"))

            for llave, dato in estudiantes.items():
                if dato["id"] == estudiantes:
                        id_estudiante = dato

                print(id_estudiante)    
                print("ESTUDIANTE ENCONTRADO")


#FUNCION PARA CONSULTAR LA LISTA DE LOS ESTUDIANTES EXISTENTE 

def consultar_estudiante():

        if opcion == "3":

            print(f"lista de estudiantes")
            
            for clave, datos in estudiantes.items():
                buscar_estudiante = datos [estudiantes]



#FUNCION PARA ELININAR ESTUDIANTES CON LA FUNCION DEL

def eliminar_estudiante():

        if opcion == "4":

            borrar = int(input("Ingresa el ID para eliminar estudiante: "))
            del (estudiantes[borrar])
            print(estudiantes)


#FUNCION PARA ACTUALZAR LA LISTA DE LOS ESTUDIANTES (DATOS: NOMBRE, ID, EDAD, CURSO)

def actualizar_estudiante():

        if opcion == "5":
            
            clave = int(input("Ingrese el numero del estudiante: "))

            if clave in estudiantes:
                estudiantes [clave] ["Nombre"] = nombre = input("Ingresa el nombre del estudiante: ")
                estudiantes [clave] ["id"] = id_estudiante = int(input("Ingresa el numero de id del estudiante: "))
                estudiantes [clave] ["edad"] = edad = int(input("Ingrese la edad del estudiante: "))
                estudiantes [clave] ["curso"] = curso = input("Ingrese el curso del estudiante: ")

                print("Actualizado")

            


# INICIO DEL WHILE (NOS PERMITE REPETIE LA OPCIONES )
continuar = True
while continuar:

#OPCIONES DEL MENU
    print("\n==================================")
    print("\n     SISTEMA DE ESTUDIANTES       ")
    print("\n==================================")
    print("1. Registrar nuevo estudiante       ")
    print("2. Buscar estudiantes               ")
    print("3. Consultar estudiantes            ")
    print("4. Eliminar estudiantes             ")
    print("5. Actualizar informacion del estudiante")
    print("6. Salir                            ")

    opcion = input("Elejir una opcion: ")









            







