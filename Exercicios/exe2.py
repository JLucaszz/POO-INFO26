expr = input().replace(" ", "")

num1 = ""
num2 = ""
operador = ""

for c in expr:
    if c in "+-*/":
        operador = c
    elif operador == "":
        num1 += c
    else:
        num2 += c

# Verificação básica
if num1 == "" or num2 == "":
    print("Entrada inválida")
else:
    num1 = int(num1)
    num2 = int(num2)

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            print("Erro: divisão por zero")
        else:
            resultado = num1 / num2

    if operador != "/" or num2 != 0:
        print("O resultado da operação é", resultado)