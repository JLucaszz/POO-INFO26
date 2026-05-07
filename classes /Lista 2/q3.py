class ContaBancaria:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f}")
        else:
            print("Valor inválido")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor <= 0:
            print("Valor inválido para saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def mostrar_saldo(self):
        print(f"Saldo Atual: R${self.saldo:.2f}")

# teste
nome = input("Nome:")
numero = input("Numero:")

conta = ContaBancaria(nome, numero)

while True:
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Valor para depósito: "))
        conta.depositar(valor)

    elif opcao == "2":
        valor = float(input("Valor para saque: "))
        conta.sacar(valor)

    elif opcao == "3":
        conta.mostrar_saldo()

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")