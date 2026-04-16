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

class Cinema:
    def __init__(self):
        self.__d = ""
        self.__h = 0 

    def set_d(self, d):
        dias_validos = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]
        if d.lower() in dias_validos:
            self.__d = d.lower()
        else: 
            raise ValueError("Dia inválido")

    def set_h(self, v):
        if 0 <= v <= 23:
            self.__h = v    
        else: 
            raise ValueError("Hora inválida")

    def get_d(self):
        return self.__d

    def get_h(self):
        return self.__h

    def __valor_base(self):
        if self.__d in ["segunda", "terca", "quinta"]:
            return 16
        elif self.__d == "quarta":
            return 8
        else: 
            return 20

    def calc_inteira(self):
        valor = self.__valor_base()
        if self.__d == "quarta":
            return 8
        if 17 <= self.__h <= 23:
            valor *= 1.5
        return valor

    def calc_meia(self):
        if self.__d == "quarta":
            return 8
        return self.calc_inteira() / 2



class UI:
    @staticmethod
    def main():
        x = Circulo()
        x.set_raio(float(input("Valor:")))
        print(x.calc_circun())

UI.main()

class UI:
    @staticmethod
    def main():
        x = Viagem()
        x.set_d(float(input("Valor d=")))
        x.set_t(float(input("Valor t=")))
        print(x.velocidade_m())
    
UI.main()

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


class UI:
    @staticmethod
    def main():
        x = Cinema()
        x.set_d("terca")
        x.set_h(15)

        print("Dia:", x.get_d())
        print("Hora:", x.get_h())
        print("Inteira:", x.calc_inteira())
        print("Meia:", x.calc_meia())


UI.main()