from ManejadorCalefactores import ManejadorCalefactores
class menu:
    opcion=None
    
    def __init__(self):
        self.__opcion=0
    def mostrarmenu(self):
        
        Tamaño = int(input('Ingrese tamaño del arreglo'))
        Obj= ManejadorCalefactores(Tamaño)

        while self.__opcion!=-1:
            print('[1]')
            print('[2] ')
            print('[3] ')
            self.__opcion=input('\nIngrese numero: ')
            if self.__opcion=='1':
                Obj.CargaArreglo()
                Obj.mostrar()
            #elif self.__opcion=='2':
               

                
            
