class Agua:
    def __init__(self, mes, ano, consumo):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo

    def calc_agua(self):
        if self.consumo <= 10:
            valor = 38
        elif self.consumo <= 20:
            valor = 38 + (self.consumo - 10) * 5
        else:
            valor = 38 + (10 * 5) + (self.consumo - 20) * 6
        return valor


# Entrada de dados
mes = input("Mês: ")
ano = input("Ano: ")
consumo = input("Consumo: ")

# Cálculo
conta = Agua(mes, ano, consumo)
valor = conta.calc_agua()

# Saída
print("Valor a pagar: R$", valor)