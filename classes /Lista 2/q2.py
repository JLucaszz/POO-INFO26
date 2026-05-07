class viagem:
    def __init__(self, distancia, horas, minutos):
        self.distancia = distancia
        self.horas = horas
        self.minutos = minutos

    def caulc_velo_media(self):
        tempo_total = self.horas + (self.minutos / 60)
        return self.distancia / tempo_total
    
# teste
distancia = float(input("KM:"))
horas = float(input("horas:"))
minuts = float(input("minuts:"))

v = viagem(distancia, horas, minuts)
velocidade = v.caulc_velo_media()
print(f"Velocidade média: {velocidade:.2f} km/h")