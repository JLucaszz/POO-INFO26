import math
def MMC(x, y):
    return abs(x * y) // math.gcd(x, y)

n1 = 10
n2 = 12
print(MMC(10, 12))