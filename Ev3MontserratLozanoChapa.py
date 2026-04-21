class Receta:
    def __init__(self, nombre, dificultad, tiempo_preparacion, calorias_porcion, num_ingredientes):
        self.__nombre = nombre
        self.__dificultad = dificultad
        self.__tiempo_preparacion = tiempo_preparacion
        self.__calorias_porcion = calorias_porcion
        self.__num_ingredientes = num_ingredientes
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
    
    @property
    def dificultad(self):
        return self.__dificultad
    
    @dificultad.setter
    def dificultad(self, valor):
        niveles = ["Facil", "Intermedia", "Avanzada"]
        if valor in niveles:
            self.__dificultad = valor
    
    @property
    def tiempo_preparacion(self):
        return self.__tiempo_preparacion
    
    @tiempo_preparacion.setter
    def tiempo_preparacion(self, valor):
        if valor > 0:
            self.__tiempo_preparacion = valor
    
    @property
    def calorias_porcion(self):
        return self.__calorias_porcion
    
    @calorias_porcion.setter
    def calorias_porcion(self, valor):
        if 0 <= valor <= 2000:
            self.__calorias_porcion = valor
    
    @property
    def num_ingredientes(self):
        return self.__num_ingredientes
    
    @num_ingredientes.setter
    def num_ingredientes(self, valor):
        if 1 <= valor <= 50:
            self.__num_ingredientes = valor