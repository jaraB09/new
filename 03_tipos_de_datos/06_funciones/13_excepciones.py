#Aileen Jara 
#28-04

#ejercicio 1 conversacion segura a numero

#objetivo: Pedir un numero al usuario y evitar errores si lo escribe 


def pedir_numero ():
    try:
        numero = int(input("Escribe un numero entero:"))
        print("!Gracias! Tu numero es:" , numero)

    except ValueError:
        print("Eso no es un numero valido. Intenta nuevamente")
pedir_numero()