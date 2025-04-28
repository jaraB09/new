pistas = ( "Puerta Roja" , 221, "Londres", 3.14, "Watson" , 7 ,"Moriarty")

#Pregunta 1 

indice = pistas.index("Puerta Roja")
print(indice)

#Pregunta 2 

print(pistas[-1])

#Pregunta 3

print(len(pistas))

#Pregunta 4 

print("Londres" in pistas)

#Pregunta 5 

pista1, pista2, pista3,*_=pistas
print({pista1},{pista2},{pista3})

#Pregunta 6


nuevas_pistas = pistas + ("Real Madrid","Universidad de Chile")
print(nuevas_pistas)

#Pregunta 7 

print(pistas.index("Watson"))

#Pregunta 8 

print(pistas.count(7))