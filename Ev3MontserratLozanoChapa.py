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

    def calcular_eficiencia(self):
        return round(self.__num_ingredientes / self.__tiempo_preparacion, 2)
    
    def obtener_categoria_salud(self):
        if self.__calorias_porcion < 300:
            return "Muy saludable"
        elif self.__calorias_porcion < 500:
            return "Saludable"
        elif self.__calorias_porcion < 800:
            return "Moderada"
        else:
            return "Alta en calorias"
        
    def info(self):

        print(f"Receta:              {self.__nombre}")
        print(f"Dificultad:          {self.__dificultad}")
        print(f"Tiempo:              {self.__tiempo_preparacion} minutos")
        print(f"Calorias:            {self.__calorias_porcion} kcal")
        print(f"Salud:               {self.obtener_categoria_salud()}")
        print(f"Ingredientes:        {self.__num_ingredientes}")
        print(f"Eficiencia:          {self.calcular_eficiencia()} ing/min")

receta = Receta("Ensalada Cesar", "Facil", 15, 350, 8)
print(receta.calcular_eficiencia())
print(receta.obtener_categoria_salud())