class Banco:
    def __init__(self):
        self.__n = ""
        self.__x = 0
        self.__s = 0
    def set_n(self, v):
        self.__n = v
    def set_x(self, v):
        if v >= 0: self.__x = v
        else: raise ValueError()
    def set_s(self, v):
        if v >= 0: self.__s = v
        else: raise ValueError()
    def get_n(self):
        return self.__n
    def get_x(self):
        return self.__x
    def get_s(self):
        return self.__s

    def depositar(self, valor):
        if valor > 0:
            self.__s += valor
        else: raise ValueError

    def sacar(self, valor):
        if valor > 0 and valor <= self.__s:
            self.__ -= valor
        else: raise ValueError()

class UI:
    @staticmethod
    def main():
        a = Banco
        a.set_n("Lucas")
        a.set_s(123)
        a.set_x(100)
        print(a.get_numero())
        print(a.get_saldo())

        a.depositar(50)
        print("Saldo após depósito:", a.get_saldo())

        a.sacar(30)
        print("Saldo após saque:", a.get_saldo())
