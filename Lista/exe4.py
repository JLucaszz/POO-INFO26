dia = int(input('Dia: '))
mes = int(input('mês: '))
ano = int(input('ano: '))

data_valida = True

if not (1 <= mes <= 12):
    data_valida = False

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 :
    if not (1 <= dia <= 31):
        data_valida = False
if mes == 4 or mes == 6 or mes == 9 or 11:
    if not (1 <= dia <= 30):
        data_valida = False
if mes == 2:
    if not (1 <= mes <= 28):
        data_valida = False
if not (1900 <= ano <= 2100):
    data_valida = False
if data_valida:
     print(f'{dia}/{mes}/{ano}')
else:
    print(f'{dia}/{mes}/{ano}')
    print("A data informada não é valida")