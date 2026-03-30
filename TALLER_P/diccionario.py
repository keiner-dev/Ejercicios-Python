#DICCIONARIOS 

hi_army = {"Nombre": "Nini",
            "Apellido": "Madero",
            "Fan": "BTS"}


print("Mi nombre:", hi_army ["Nombre"] )
print("Mi apellido:", hi_army ["Apellido"])
print("Soy fan de:", hi_army ["Fan"])




Coders = {
1: {
      "Nombre": "Elianis",
      "Apellido": "Cervnates",
      "id": "1043585751"
      },

2: {
      "Nombre": "Deyanis",
      "Apellido": "Martero",
      "id": "130586333"
            },
      
3: {
      "Nombre": "Angela",
      "Apellido": "Manjares",
      "id": "10564745"
      },
      }


continuar = True
while continuar: 

      print(" ===== MENU DE CODERS=====")
      print("1. Agregar coder")
      print("2. Buscar coder")
      print("3. Eliminar coder")
      print("4. Salir")

      opcion = input("Elige una opcion: ")

# AGREGAR CODERS  

      if opcion == "1": 
            id_coder = int(input("Ingresa el documento: "))
            nombre = input("Ingresa tu nombre: ")
            apellido = input("Ingresa tu apellido: ")

            Coders[4]  = {
                  "nombre": nombre,
                  "apellido": apellido,
                  "id": id_coder,
            }

            print(f"Coder {nombre} {apellido} agregado con exito")

#BUESCAR CODERS

      if opcion == "2":

            id_coder = int(input("Ingresa el N° documento para la busqueda: "))
            id_coder = None

            print("Buscando por N° de documento")
            print("Buscando con metodo get")
            print(Coders.get(1, "No encontrado"))

            for llave, dato in Coders.items():
                  if dato["id"] == id_coder:
                        id_coder = dato

                  print(id_coder)    
                  print("Coder encontrado ")

#ELIMINAR CODERS

      if opcion == "3":

            borrar = int(input("Ingresa el ID para eliminar coders: "))
            del (Coders[borrar])
            print(Coders)


      elif opcion == "4":
            print("Salir")
            









