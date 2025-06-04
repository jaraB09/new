#Aileen Jara 
#to fomekee queremos vacaciones :/
# Actualizar valores en diccionarios y listas

#Matriz original
matriz = [[10, 15, 20], [3, 7, 14]]

#Cambiar el valor de 3 por 6
matriz[1][0] = 6

# Lista de cantantes
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

#Cambiar el nombre del primer cantante
cantantes[0]["nombre"] = "Enrique Martin Morales"

#Diccionario de ciudades
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

#Cambiar "Cancún" por "Monterrey"
ciudades["México"][2] = "Monterrey"

#Lista de coordenadas
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

#Cambiar el valor de "latitud"
coordenadas[0]["latitud"] = 9.9355431

#Imprimir resultados
print("Matriz actualizada:", matriz)
print("Cantantes actualizados:", cantantes)
print("Ciudades actualizadas:", ciudades)
print("Coordenadas actualizadas:", coordenadas)





def iterarDiccionario(lista):
    for diccionario in lista:
        print(", ".join(f"{llave} - {valor}" for llave, valor in diccionario.items()))

#Lista de cantantes para probar la función
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

#Llamar a la función con la lista de cantantes
iterarDiccionario(cantantes)



def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

#Ejemplo de uso
iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)




def imprimirInformacion(diccionario):
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print(valor)

#Ejemplo de uso
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

imprimirInformacion(costa_rica)