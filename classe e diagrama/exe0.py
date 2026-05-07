class Retangulo:
    def __init__(self):
        self.__base = 0 
        self.__altura = 0
    def set_base(self, valor):
        if valor < 0: raise ValueError("valor deve ser positivo")
        self.__base = valor
    def get_base(self):
        return self.__base
    def set_altura(self, valor):
        if valor < 0: raise ValueError("valor deve ser positivo")
        self.__altura = valor
    def get_altura(self):
        return self.__altura
    def diagonal(self):
        return (self.__base ** 2 + self.__altura ** 2) ** 0.5 

class UI:
    def main():
        x = Retangulo()
        x.set_base(float(input("Valor 1:")))
        x.set_altura(float(input("Valor 2:")))
        print(f"o retangulo de base {x.set_base()} e altura {x.set_altura()}")
        diagonal = x.diagonal()
        print(f"tem diagonal {diagonal}")

UI.main()