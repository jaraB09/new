#Aileen Jara 
#14-04

altura = int(input("¿Cuanto mides?"))
creditos = int(input("¿Cuantos creditos tienes ?"))

if altura >=137 and creditos >=10:
   print('Disfruta el viaje')

elif altura >137 and creditos >=10:
    print("No eres lo sufciente alto para viajar")

elif altura >137 and creditos >10:
    print("No tienes suficiente creditos para viaje")

else:
    print('No cumples los requisitos para viajar')
