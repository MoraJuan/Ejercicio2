
class Viajero:
    __numviajero = int
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas= int
     
    def __init__(self, numviajero, dni, nombre, apellido, millas):
         self.__numviajero = numviajero
         self.__dni = dni
         self.__nombre = nombre
         self.__apellido = apellido
         self.__millas = millas
         
    def __str__(self):
        return str(self.__numviajero)
                
   
    def cantidadTotaldeMillas(self):
        return 'Cantidad de millas realizadas \n' + str(self.__millas)
    
    #def Acummillas(self):        