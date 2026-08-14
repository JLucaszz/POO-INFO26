from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento

    def get_nome(self): return self.__nome
    def set_nome(self, v): self.__nome = v

    def get_cpf(self): return self.__cpf
    def set_cpf(self, v): self.__cpf = v

    def get_telefone(self): return self.__telefone
    def set_telefone(self, v): self.__telefone = v

    def get_nascimento(self): return self.__nascimento
    def set_nascimento(self, v): self.__nascimento = v

    def idade(self):
        hoje = datetime.now()
        
        anos = hoje.year - self.__ano
        meses = hoje.month - self.__mes

        if hoje.day < self.__dia:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12
        return f"{anos} anos e {meses} meses"

    def __str__(self):
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Tel: {self.__telefone}"

