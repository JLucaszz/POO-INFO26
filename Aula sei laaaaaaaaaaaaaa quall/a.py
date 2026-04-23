class Retangulo:
    def __init__(self, b, h):
        self.__b = 0  
        self.__h = 0
        self.set_base(b)
        self.set_altura(h)
    def set_base(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_base(self, v):
        if v >= 0: self.__h = v
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_base(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h
    def __str__(self):
        return f"base = {self.__b} - altura = {self.__h}"
    def calc_diagonal(self):
        return (self.__b ** 2 + self.__h ** 2) ** (1/2)
        