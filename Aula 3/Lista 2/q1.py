import math
class circulo:
    def __init__(self, raio):
        self.raio = raio 

    def calc_area(self):
        return math.pi * (self.raio ** 2)
    
    def calc_circunferencia(self):
        return 2 * math.pi * self.raio
    
# teste
raio = float(input("Exemplo:"))

c = circulo(raio)
print(f"Área: {c.calc_area():.2f}") 
print(f"Circunferência: {c.calc_circunferencia():.2f}")