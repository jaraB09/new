#Acceder a un valor en un diccionario 
#sin que se rompa el programa si la clave no existe 

def buscar_cantante():
    cantate={
        "nombre" : "Luis Miguel" ,
        "pais" : "puerto rico"
    }

    try:
        clave = int("¿Que quieres saber? (nombre o pais):")
        print("Resultado:" , cantante[clave])

    except KeyError:
        print("Esta clave no existe")

buscar_cantante


