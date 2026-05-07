class Viagem:
    def __init__(self, dest: str, dist: float, lt: float):
        self.set_destino(dest)
        self.set_distancia(dist)
        self.set_litros(lt)

    def set_destino(self, v):
        if v != '':
            self.__destino = v
        else:
            raise ValueError("Destino inválido")

    def set_distancia(self, v):
        if v >= 0:
            self.__distancia = v
        else:
            raise ValueError("Distância inválida")

    def set_litros(self, v):
        if v > 0:
            self.__litros = v
        else:
            raise ValueError("Litros deve ser maior que zero")

    def get_destino(self):
        return self.__destino

    def get_distancia(self):
        return self.__distancia

    def get_litros(self):
        return self.__litros

    def consumo(self):
        return self.__distancia / self.__litros

    def __str__(self):
        return f"Destino: {self.__destino}, Distância: {self.__distancia} km, Litros: {self.__litros}"


class Pais:
    def __init__(self, n: str, p: int, a: float):
        self.set_nome(n)
        self.set_populacao(p)
        self.set_area(a)

    def set_nome(self, v):
        if v != '':
            self.__nome = v
        else:
            raise ValueError("Nome inválido")

    def set_populacao(self, v):
        if v >= 0:
            self.__populacao = v
        else:
            raise ValueError("População inválida")

    def set_area(self, v):
        if v > 0:
            self.__area = v
        else:
            raise ValueError("Área deve ser maior que zero")

    def get_nome(self):
        return self.__nome

    def get_populacao(self):
        return self.__populacao

    def get_area(self):
        return self.__area

    def densidade(self):
        return self.__populacao / self.__area

    def __str__(self):
        return f"Nome: {self.__nome}, População: {self.__populacao}, Área: {self.__area} km²"


class UI:
    @staticmethod
    def main():
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1:
                UI.calculo_v()
            elif op == 2:
                UI.calculo_p()

    @staticmethod
    def menu():
        print("\n1 - Calcular viagem")
        print("2 - Calcular país")
        print("3 - Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def calculo_v():
        dest = input("Destino: ")
        dist = float(input("Distância (km): "))
        lt = float(input("Litros usados: "))

        x = Viagem(dest, dist, lt)
        print(x)
        print(f"Consumo médio: {x.consumo():.2f} km/l")

    @staticmethod
    def calculo_p():
        nom = input("Nome do país: ")
        popu = int(input("População: "))
        are = float(input("Área (km²): "))

        x = Pais(nom, popu, are)
        print(x)
        print(f"Densidade demográfica: {x.densidade():.2f} hab/km²")


UI.main()