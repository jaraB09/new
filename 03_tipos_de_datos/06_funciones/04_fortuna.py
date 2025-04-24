#Aileen Jara 
#14-04
#EN LA MEA FOMEEEE 

import random

opciones = [
    "no persigas la felicidad,  creala"
    "todas las cosas son dificiles antes de ser faciles"
    "el pajaro madrugador consigue el gusano, pero el segundo raton se llama queso"
    "alguien en tu vida necesita una carta de tu parte"
    "no solo pienses. actua"
    "la fortuna que vbuscas esta en otra galleta"
    "¡Ayuda! ¡que estoy prisionero en una panaderia china"
    
]

def fortuna():
    fortuna = random.randint(0, len(opciones)-1)
    print(opciones[fortuna])


fortuna()
fortuna() 
fortuna()   
