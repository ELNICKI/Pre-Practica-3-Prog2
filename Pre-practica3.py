class vehiculo: 
    def __init__(self,marca:str ,ruedas:int,color:str,enMarcha:bool=False):
        self.marca:str=marca
        self.ruedas:int=ruedas
        self.color:str=color
        self.enMarcha:bool=enMarcha
    def arrancar(self):
        self.enMarcha = True
    def tipoVehiculo(self):
        if self.ruedas == 2:
            return "Motocicleta"
        elif self.ruedas == 4:
            return "Auto"
        else: 
            return "Camión"
    def mostrar(self):
        return self.marca, self.ruedas , self.color , self.enMarcha



"""
Comisión : 2
Grupo : 5
Integrantes: Augusto Camani, Santiago Feresin, Nicolás Martinez
Legajo:     50525          , 50837           , 50630

"""