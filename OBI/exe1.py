p = input("Digite a palavra:")
vogais = "aeiou"
alfabeto = "abcefghijklmnopqrstuvwxyz"

for a in p: 
    if a in vogais:
        print(a, end="")
    else:
        menor = 100
        vogal_proxima = ""

        for b in vogais:
            distancia = abs(ord(a) - ord(b))
            if distancia < menor:
                menor = distancia
                vogal_proxima = b
        i = 0
        while alfabeto[i] != a:
            i += 1

        i += 1
        while i < len(alfabeto) and alfabeto[i] in vogais:
            i += 1

        if i < len(alfabeto):
            proxima_consoante = alfabeto[i]
        else:
            proxima_consoante = a

        print(a + vogal_proxima + proxima_consoante, end="")

