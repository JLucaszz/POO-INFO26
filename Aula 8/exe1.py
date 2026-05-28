from enum import Enum
from datetime import datetime

class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3


class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        # Atributos que vão ser validados
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor_boleto(valor)
        # Atribuida com valor inicial pré-definido
        self.__data_pagto = None
        self.__valor_pago = 0
        self.__situacao_pagamento = Pagamento.EM_ABERTO

    def set_cod_barras(self,cod):
        if len(cod) != 10: raise ValueError()
        self.__cod_barras = cod

    def set_data_emissao(self, emissao):
        if emissao > datetime.now(): raise ValueError()
        self.__data_emissao = emissao

    def set_data_vencimento(self, venc):
        if venc < datetime.now(): raise ValueError()
        self.__data_vencimento = venc

    def set_valor_boleto(self, valor):
        if valor < 0: raise ValueError()
        self.__valor_boleto = valor

    def pagar(self, valor_pago):
        if valor_pago < 0: raise ValueError()
        if self.__situacao_pagamento != Pagamento.EM_ABERTO: raise ValueError()
        self.__valor_pago = valor_pago
        self.__data_pagto = datetime.now()
        if self.__valor_boleto == self.__valor_pago: self.__situacao_pagamento = Pagamento.PAGO
        else: self.__situacao_pagamento = Pagamento.PAGO_PARCIAL

    def get_cod_barras(self): return self.__cod_barras
    def get_data_emissao(self): return self.__data_emissao
    def get_data_vencimento(self): return self.__data_vencimento
    def get_valor_boleto(self): return self.__valor
    def get_situacao_pagamento(self): return self.__situacao_pagamento
    def valor_pago(self): return self.__valor_pago
    def data_pagto(self): return self.__data_pagto

    def __str__(self):
        s = f"Boleto: {self.__cod_barras} - Emissão: {self.__data_emissao.strftime('%d/%m/%Y')}"
        s += f"Valor: R$ {self.__valor_boleto:.2f} - Valor Pago: R$ {self.__valor_pago}"
        s += f"Vencimento: {self.__data_emissao.strftime('%d/%m/%Y')}"
        s += f"Data de Pagamento: {self.__data_pagto}"
        s += f"Situação; {self.__situação_pagamento}"
        return s
    
    




