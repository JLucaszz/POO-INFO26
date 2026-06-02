from enum import Enum
from datetime import datetime

class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor_boleto(valor)
        
        self.__data_pagamento = None
        self.__valor_pago = 0.0
        self.__situacao_pagamento = Pagamento.EM_ABERTO

    def set_cod_barras(self, cod):
        if len(cod) != 10: 
            raise ValueError("Código deve ter 10 dígitos")
        self.__cod_barras = cod

    def set_data_emissao(self, emissao):
        if emissao > datetime.now(): 
            raise ValueError("Data não pode ser no futuro")
        self.__data_emissao = emissao

    def set_data_vencimento(self, venc):
        self.__data_vencimento = venc

    def set_valor_boleto(self, valor):
        if valor < 0: 
            raise ValueError("Boleto não pode ter valor negativo")
        self.__valor_boleto = valor    

    def pagar(self, valor_pago):
        if valor_pago < 0: 
            raise ValueError("Valor pago não pode ter valor negativo")
        if self.__situacao_pagamento == Pagamento.PAGO: 
            raise ValueError("Boleto já foi totalmente pago")
            
        self.__valor_pago = valor_pago
        self.__data_pagamento = datetime.now()
        
        if self.__valor_pago >= self.__valor_boleto: 
            self.__situacao_pagamento = Pagamento.PAGO
        else: 
            self.__situacao_pagamento = Pagamento.PAGO_PARCIAL

    def get_cod_barras(self): return self.__cod_barras   
    def get_data_emissao(self): return self.__data_emissao  
    def get_data_vencimento(self): return self.__data_vencimento
    def get_valor_boleto(self): return self.__valor_boleto  
    def get_valor_pago(self): return self.__valor_pago   
    def get_data_pagto(self): return self.__data_pagamento 
    def get_situacao_pagamento(self): return self.__situacao_pagamento
    
    def situacao(self): 
        return self.__situacao_pagamento
    
    def __str__(self): 
        s = f"Boleto: {self.__cod_barras} - Emissão: {self.__data_emissao.strftime('%d/%m/%Y')}\n"
        s += f"Valor: R$ {self.__valor_boleto:.2f} - Valor Pago: R$ {self.__valor_pago:.2f}\n"
        s += f"Vencimento: {self.__data_vencimento.strftime('%d/%m/%Y')}\n"
        if self.__data_pagamento is not None:
            s += f"Data de Pagamento: {self.__data_pagamento.strftime('%d/%m/%Y')}\n"
        s += f"Situação: {self.__situacao_pagamento.name}"
        return s
    
class BoletoUI:
    __boletos = []

    @staticmethod
    def main():
        op = 0
        while op != 10:
                op = BoletoUI.menu()
                if op == 1: BoletoUI.inserir()
                elif op == 2: BoletoUI.listar()
                elif op == 3: BoletoUI.atualizar()
                elif op == 4: BoletoUI.excluir()
                elif op == 5: BoletoUI.boletos_em_aberto()
                elif op == 6: BoletoUI.boletos_pagos()
                elif op == 7: BoletoUI.boletos_a_vencer()
                elif op == 8: BoletoUI.boletos_vencidos()
                elif op == 9: BoletoUI.pagar_boleto()
                return int(input("escolha uma opção: "))
    
    @staticmethod
    def menu():
        print("\n---------------------------------------------")
        print(" 1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir ")
        print(" 5-Boletos em Aberto, 6-Boletos Pagos        ")
        print(" 7-Boletos a Vencer,  8-Boletos Vencidos     ")
        print(" 9-Pagar Boleto,      10-Sair                ")
        print("---------------------------------------------")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def inserir(cls):
        cod = input("Informe o código do boleto com 10 dígitos: ") 
        emissao = datetime.strptime(input("Informe a data de emissão dd/mm/aaaa: "), "%d/%m/%Y")
        venc = datetime.strptime(input("Informe a data de vencimento dd/mm/aaaa: "), "%d/%m/%Y")
        valor = float(input("Informe o valor: "))
        x = Boleto(cod, emissao, venc, valor)
        cls.__boletos.append(x)
        print("Boleto inserido com sucesso!")
    
    @classmethod
    def listar(cls):
        if not cls.__boletos:
            print("Nenhum boleto cadastrado.")
        for x in cls.__boletos: 
            print("\n" + str(x))
    
    @classmethod
    def atualizar(cls):
        cod = input("Digite o código do boleto que você deseja atualizar: ")
        for x in cls.__boletos:
            if x.get_cod_barras() == cod:
                nova_emissao = datetime.strptime(input("Informe a nova data de emissão dd/mm/aaaa: "), "%d/%m/%Y")
                novo_venc = datetime.strptime(input("Informe a nova data de vencimento dd/mm/aaaa: "), "%d/%m/%Y")
                novo_valor = float(input("Informe o novo valor: "))
                
                x.set_data_emissao(nova_emissao)
                x.set_data_vencimento(novo_venc)
                x.set_valor_boleto(novo_valor)
                print("Boleto atualizado com sucesso!")

    @classmethod
    def excluir(cls):
        cod = input("Digite o código do boleto que você deseja remover: ")
        for x in cls.__boletos:
            if x.get_cod_barras() == cod:
                cls.__boletos.remove(x)
                print("Boleto removido")
               

    @classmethod
    def boletos_em_aberto(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamento() == Pagamento.EM_ABERTO:
                print("\n" + str(x))
                

    @classmethod
    def boletos_pagos(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamento() in [Pagamento.PAGO, Pagamento.PAGO_PARCIAL]:
                print("\n" + str(x))

    @classmethod
    def boletos_a_vencer(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamento() == Pagamento.EM_ABERTO and x.get_data_vencimento() >= datetime.now():
                print("\n" + str(x))

    @classmethod
    def boletos_vencidos(cls):
        for x in cls.__boletos:
            if x.get_situacao_pagamento() == Pagamento.EM_ABERTO and x.get_data_vencimento() < datetime.now():  
                print("\n" + str(x))

    @classmethod
    def pagar_boleto(cls):
        cod = input("Digite o código do boleto que você quer pagar: ")
        for x in cls.__boletos:
            if x.get_cod_barras() == cod:
                if x.get_situacao_pagamento() == Pagamento.EM_ABERTO:
                    valor = float(input(f"Valor do boleto é R${x.get_valor_boleto():.2f}. Digite o valor pago: "))
                    x.pagar(valor)
                    print("Pagamento registrado")

BoletoUI.main()