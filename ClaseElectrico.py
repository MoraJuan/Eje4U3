from ClaseCalefactor import ClaseCalefactor
class ClaseElectrico(ClaseCalefactor):
    __potencia = None
    
    def __init__(self,marca, modelo, potencia):
        super().__init__(marca, modelo)
        self.__potencia = potencia  
