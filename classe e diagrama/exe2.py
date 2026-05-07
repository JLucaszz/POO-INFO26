class Viagem:
    def __init__(self):
        self.__d = 0 
        self.__t = 0
    def set_d(self, v):
        if v >= 0: self.__d = v
        else: raise ValueError()
    def set_t(self, v):
        if v >= 0: self.__t = v
        else: raise ValueError()
    def get_d(self):
        return self.__d
    def get_t(self):
        return self.__t
    def velocidade_m(self):
        return self.__d / self.__t
    
class UI:
    @staticmethod
    def main():
        x = Viagem()
        x.set_d(float(input("Valor d=")))
        x.set_t(float(input("Valor t=")))
        print(x.velocidade_m())
    
UI.main()