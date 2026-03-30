a = [15,35,56,70,72,85,90,101,105]
#    0   1  2  3  4  5  6  7   8

izq = 0 
derech = len (a) -1
med =(izq + derech) // 2

sw = False
b = int(input("Ingresa un numero de la lista: "))

sw = False
while sw == False and izq >= derech:
    
    med = (izq + derech) //2
    if a[med] == b:
        print("Numero encontrado")
        sw = True

    elif [med] > b:
        derech = med
        med = (izq + derech ) // 2 - 1

    else:
        izq = med + 1
        med = (izq + derech) // 2
        print("Numero no encontrado")