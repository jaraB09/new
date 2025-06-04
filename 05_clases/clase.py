class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza 
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def atributos (self):
        print(self.__nombre,";", sep="")
        print("Fuerza:", self.__fuerza)
        print("Inteligencia:", self.__inteligencia)
        print("Defensa:", self.__defensa)
        print("Vida:", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa   

    def esta_vivo(self):
        return self.__vida> 0
    
    def morir (self):
        self.__vida = 0
        print(self.__nombre, "Has Muerto")

    def daño (self, enemigo):
        return self.__fuerza - enemigo.__defensa
    
    def atacar(self, enemigo):
        daño =self.__daño(enemigo)
        enemigo.__vida = enemigo.__vida -daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        if enemigo.__esta_vivo():
         print("La vida de", enemigo.__nombre, "es", enemigo.__vida)
        else:
            enemigo.__morir()

    def get_fuerza(self, fuerza):
        if fuerza < 0:
            print("error, has introducido un valor negativo")
        self.__fuerza = fuerza


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    def cambiar_arma(self):
        opcion = int(input("elige un arma: (1) acero valyro, daño 8 (2) matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("ingresa una opcion valida")
    def atributos(self):
        super().atributos()
        print("Espada:", self.espada)
   
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, magia):
        super().init__(nombre, fuerza, inteligencia, defensa, vida)
        self.Libro = Libro
    def atributos(self):
        super().atributos()
        print("Libro:", self.Libro)
    def daño(self, enemigo):
        return self.inteligencia * self.Libro - enemigo.defensa
 
kaldrogo = Guerrero("Kaldrogo", 20, 30, 20, 100, 5)
mi_personaje = Personaje("Fabian", 10, 20, 10, 100)
gandalf = Mago("Gandalf", 20, 30, 20, 100, 5)


kaldrogo.atributos()
print("____________________________")
mi_personaje.atributos()
print("____________________________")
gandalf.atributos()
print("____________________________")

mi_personaje.atacar(kaldrogo)
kaldrogo.atacar(gandalf)
gandalf.atacar(mi_personaje)
#mi_enemigo = Personaje("Blastor", 8, 5, 3, 5)
#mi_personaje.atacar(mi_enemigo)
#mi_personaje.atributos() 

