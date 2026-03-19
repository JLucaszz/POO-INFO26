l = []
for x in range(4):
    n = int(input())
    if n not in l: l.append(n)
    else: print("Insira valores difentes um do outro")
l.sort()
print(f'Maior valor = {l[3]}')
print(f'menor valor = {l[0]}')
print(f'A soma do segundo maior valor com o segundo menor = {l[1] + l[2]}')