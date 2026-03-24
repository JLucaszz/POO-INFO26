class Triângulo:
    def __init__(self):
        self.b = 0            #atributos
        self.h = 0            
    def calc_area(self):      #método
        return self.b * self.h / 2
    
x = Triângulo()               # chama o método __init__
print(x.b, x.h)
x.b = float(input("Informe a base do triângulo\n"))
x.h = float(input("Informe a aultura do triângulo\n"))
print(x.b, x.h)
a = x.calc_area()
print(f"A área do segundo triângulo é {a:.2f}")

y = Triângulo()
print(y.b, y.h)
y.b = float(input("Informe a base do segundo triângulo\n"))
y.h = float(input("Informe a aultura do segundo triângulo\n"))
print(y.b, y.h)
a = y.calc_area()
print(f"A área do segundo triângulo é {a:.2f}")