class Pais:
    def __init__(self, nome, populacao, area):
        self.nome = nome
        self.populacao = populacao
        self.area = area

    def calc_densidade(self):
        return self.populacao / self.area


n = input()
p = int(input())
a = float(input())

s = Pais(n, p, a)

densidade = s.calc_densidade()

print("A densidade demográfica do", s.nome, "é de %.2f hab/km2" % densidade)