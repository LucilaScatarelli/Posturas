class Posturas():

    def __init__(self,clasificacion,serie):
        self.clasificacion=clasificacion
        self.serie=serie
        self.ejecutandose=False
    
    def ejecutar(self):
        self.ejecutandose=True

    def estado(self):
        print("Clasificacion:",self.clasificacion,"\nSerie:",self.serie, "\nEn ejecución: ",self.ejecutandose)  


class Yoga(Posturas):
    pass

print("--------------Postura 1--------------")

padahastasana=Yoga("Postura de Pie","Primera Serie")
padahastasana.estado()


print("--------------Postura 2--------------")

trikonasana=Yoga("Postura de pie","Primera Serie")
trikonasana.ejecutar()
trikonasana.estado()