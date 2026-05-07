frase = input()
soma = 0

for c in frase:
    if c >= '0' and c <= '9':
        soma += int(c)

print(soma)