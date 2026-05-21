from datetime import datetime, timedelta

nasc = datetime.strptime(input("Informe a data de Nascimento: "), "%d/%m/%Y")
hoje = datetime.now()

x = hoje - nasc
print(x)

anos = x.days // 365
print(anos, "anos")

meses = x.days % 365 // 30
print(meses, "meses")

dias = x.days % 30
print(dias, "dias")