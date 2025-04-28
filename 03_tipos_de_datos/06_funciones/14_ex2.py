#Aileen Jara 
#28-04

#objetivo dividir entre 2 numeros y evitar o alertar 
#si el usuario quiere dividir entre 0

def division_segura():
    try:
        num1 = int(input("Ingresa un numero:"))
        num2 = int(input("Ingresa otro numero:"))
        resultado = num1 / num2 

        print("el resultado de la division es:" , resultado)

    except ZeroDivisionError:
        print("Lo sentimos no se puede realizar esta division")

    except ValueError:
        print("Error. Solo debes ingresar numeros")

    division_segura() bb