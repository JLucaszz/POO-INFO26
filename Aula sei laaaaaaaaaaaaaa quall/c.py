class Equação:
    def __init__(self, a, b, c, d):
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)
        self.set_d(d)
    def set_a(self, v):
        if v != 0: self.__a = v
        else: raise ValueError()
    def set_b(self, v):
        if v >= 0: self.__b = v
        else: raise ValueError()
    def set_c(self, v):
        if v >= 0: self.__c = v
        else: raise ValueError()
    def set_d(self, v):
        if v >= 0: self.__d = v
        else: raise ValueError()
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b
    def get_c(self):
        return self.__c
    def get_(self):
        return self.__d
    def calc_delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
    def tem_real(self):
        return self.d() >= 0
    def raiz1(self):
        if not self.tem_real():
            raise ValueError("Não possui raízes reais")
        return (-self.__b + (self.delta() ** 0.5)) / (2*self.__a)
    def raiz2(self):
        if not self.tem_real():
           raise ValueError("Não possui raízes reais")
        return (-self.__b - (self.delta() ** 0.5)) / (2*self.__a)
    def toString(self):
        return f"a={self.__a}, b={self.__b}, c={self.__c}"

    



