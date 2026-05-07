class Pais:
    def __init__(self, nome, populacao, area):
        self.nome = nome
        self.populacao = populacao
        self.area = area

    def calc_densidade(self):
        return self.populacao / self.area


paises = []

# Ler dados
for i in range(10):
    print(f"\nPaís {i+1}")
    nome = input("Nome: ")
    populacao = int(input("População: "))
    area = float(input("Área: "))

    paises.append(Pais(nome, populacao, area))

# Encontrar maior densidade
maior = paises[0]

for p in paises:
    if p.calc_densidade() > maior.calc_densidade():
        maior = p

# Mostrar resultado
print("\nMaior densidade:")
print("Nome:", maior.nome)
print("Densidade:", maior.calc_densidade())