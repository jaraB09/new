#mostrar  un elemento de una lista por su posicion, ,manejando si la
#posicion no existe 

def mostrar_elemento():
    frutas = ["manzana" , "banana", "naranja", "palta"]
try:
        indice = int(input("elige una posicion (0 a 3):"))
        print("fruta elegida:" , frutas[indice])

except IndexError:
    print("Esta posicion no existe en la lista")


except ValueError:
    print("Debes ingresar numero")

mostrar_elemento()