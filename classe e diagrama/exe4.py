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
        x = Cinema()
        x.set_d("terca")
        x.set_h(15)

        print("Dia:", x.get_d())
        print("Hora:", x.get_h())
        print("Inteira:", x.calc_inteira())
        print("Meia:", x.calc_meia())


UI.main()