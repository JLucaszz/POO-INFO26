class Circulo:
    def __init__(self):
        self.__raio = 0
        self.__pi = 3.14
    def set_raio(self, v):
        if v >= 0: self.__raio = v
        else: raise ValueError()
    def get_raio(self):
        return self.__raio
    def calc_area(self):
        return self.__pi * self.__raio ** 2
    def calc_circun(self):
        return 2 * self.__pi * self.__raio

class UI:
    @staticmethod
    def main():
        x = Circulo()
        x.set_raio(float(input("Valor:")))
        print(x.calc_circun())

UI.main()