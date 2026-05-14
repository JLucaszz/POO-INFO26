a = int(input(""))
b = int(input(""))
c = int(input(""))

l = [a, b, c]

menor = min(l)
maior = max(l)

meio = sum(l) - maior - menor
print(meio)