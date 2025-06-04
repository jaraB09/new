#Aileen Jara 
#26-05
#se cayo el cielo dijo el chicklen little

class Libro:
    def __init__(self, titulo, autor, paginas, genero, copias_disponible):
        self.titulo = titulo
        self.autor = autor 
        self.paginas = paginas 
        self.genero = genero
        self.copias_disponible = copias_disponible

    def atributos(self):
        print(self.titulo,":",sep="")
        print("*Autor",self.autor)
        print("*Paginas",self.paginas)
        print("*Genero",self.genero)
        print("*Copias Disponibles", self.copias_disponible)
    
    def incrementar_copias(self, nuevas_copias):
        self.copias_disponible = self.copias_disponible + nuevas_copias
    
    def esta_disponible(self):
        return self.copias_disponible > 0
    
    def agotado(self):
        self.copias_disponible == 0
        print(self.titulo, "agotado")
    
    def prestar(self, copias=1):
        if self.copias_disponiblev >= copias:
            self.copias_disponible -=copias
            print(f"Has prestado{copias} copias(s) de '{self.titulo}'.")

        else:
            print(f"No hay suficientes copias disponiblesde de '{self.titulo}'para prestar {copias} copias.")
        

mi_libro = Libro("El Principito", "Antonine de Saint-Exupery", 154,"cuento",10)
mi_libro.prestar(2)
mi_libro.atributos


print(mi_libro)
print("el titulo de libro es:", mi_libro.titulo)
print("el titulo de libro es:", mi_libro.autor)

#como inicializar sin inicializarse
#que sentencia indica que no haga de momento
#como metregarle valores a la base
#cmo se llama la funcion de la clase 
#como accedo a los valores de un objecto 
#que es self
#para que sirve sep=
#como creamos el metodo de atributos de una clase
#cmo llamamos al metodo de atributos de la clase