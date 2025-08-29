#Creamos función que formatee enteros a cadena en el formato específico deseado:
def formatear(h, m, s):
    return f"{h:02d}:{m:02d}:{s:02d}"

#Creamos nuestra clase principal:
class Temporizador:
    #Creamos constructor con sus argumentos y propiedades de objeto (privadas) pertinentes:
    def __init__(self, horas = 0, minutos = 0, segundos = 0):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    #Definimos un método que incremente correctamente y segundo a segundo nuestro temporizador:
    def siguiente_segundo(self):
        self.__segundos += 1
        if self.__segundos == 60:
            self.__segundos = 0
            self.__minutos += 1
            if self.__minutos == 60:
                self.__minutos = 0
                self.__horas += 1
                if self.__horas == 24:
                    self.__horas = 0

    #Definimos un método que decremente correctamente y segundo a segundo nuestro temporizador:
    def anterior_segundo(self):
        self.__segundos -= 1
        if self.__segundos == -1:
            self.__segundos = 59
            self.__minutos -= 1
            if self.__minutos == -1:
                self.__minutos = 59
                self.__horas -= 1
                if self.__horas == -1:
                    self.__horas = 23
                    
    #Definimos un método que invoque la función externa que se ocupa de la conversión a cadena:            
    def __str__(self):
        return formatear(self.__horas, self.__minutos, self.__segundos)
    
#Creamos objeto:
temporizador = Temporizador(23, 59, 59)

#Realizamos diferentes comprobaciones usando los métodos previamente creados:
print(temporizador)
temporizador.siguiente_segundo()
print(temporizador)
temporizador.anterior_segundo()
print(temporizador)