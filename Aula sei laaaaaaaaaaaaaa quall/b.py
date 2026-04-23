class Frete:
    def __init__(self, d, p):
        self.__d = 0
        self.__p = 0
        self.set_distacia(d)
        self.set_peso(p)
    def set_distancia(self, v):
        if v >= 0: self.__d = v
        else: raise ValueError()
    def set_peso(self, v):
        if v >= 0: self.__p = v
        else: raise ValueError()
    def get_distancia(self):
        return self.__d
    def get_peso(self):
        return self.__p
    def calc_frete(self):
        return self.__d * self.__p * 0.01
    def __str__(self):
        return f"Distancia = {self.__d} - Peso = {self.__p}"