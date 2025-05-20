#Aileen Jara 
#31-03
#Vamossss 

import random

# Lista de respuestas posibles de la bola mágica 8 
respuestas = [
      "Si, definitivamente",
      "Con toda certeza, que sí",
      "Sin lugar a dudas",
      "Respuesta confusa, inténtelo de nuevo",
      "Pregúntelo nuevamente más tarde",
      "Nejor no decirte ahora",
      "Mis fuentes dicen que no"
      "El panorama no es muy favorable",
      "Muy dudoso"
]

# Función principal 
def bola_8():
    pregunta = input ("Pregunte:")
    respuesta = random.choice(respuestas)
    print(f"Magic 8 Ball: {respuesta}")

# Ejecutar el programa
if _name_ == "_main_":
   bola_8()