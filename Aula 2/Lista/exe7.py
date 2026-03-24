frase = input("Digite uma frase: ")
corte = frase.split()
while len(corte) > 0:
    frase_atual = ' '.join(corte)
    print(frase_atual)
    corte = corte[1:]