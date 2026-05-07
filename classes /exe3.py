x = [1, 2, 3]
y = x 
y.append(4)
print(x)
class Triângulo:
    def __init__(self):
        self.b = 0           
        self.h = 0            
    def calc_area(self):      
        return self.b * self.h / 2

x = Triângulo()
print(x)
y = x 