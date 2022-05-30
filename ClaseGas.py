from ClaseCalefactor import ClaseCalefactor

class ClaseGas(ClaseCalefactor):
    __matricula = None
    __calorias = None

    def __init__(self,marca, modelo, matricula, calorias):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = calorias
    
    def getMatricula(self):
        return self.__matricula
        

