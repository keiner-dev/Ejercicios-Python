#TUPAS ENTRE TUBLAS 

#t = (
 #   ("Helado, 1500"), 
#     ("Bolis, 1200"), 
 #    ("Raspado, 2500")
#)

#print("el precio del es: ", t[2], [0]) 



#Crear lsita:

lista = []

n = input("Ingresa el tamaño de tu lista: ")
m = input("ingresa el tamaño sulista: ")

for i in range(0,n,1):
    for j in range(0,m,1):
        lista[i][j] = input("Ingresa un caracte: ")

for i in range (0,n,1):
    for j in range (0,m,1): 
        print(lista[i][j])

    print("\n")   



