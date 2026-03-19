def Primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input('Número: '))

if Primo(n):
    print('É primo')
else: 
    print('Não é primo')