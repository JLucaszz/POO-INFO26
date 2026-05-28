import enum 

class Estacao(enum.Enum):
    OUTONO = 1
    INVERNO = 2
    PRIMAVERA = 3
    VERÃO = 4

a = Estacao.INVERNO
b = Estacao["VERÃO"]
c = Estacao(3)

print(a)
print(b)
print(c)
print(a.name)
print(a.value)


