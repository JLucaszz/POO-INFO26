from models.atendimento import Atendimento
import json

class AtendimentoDAO:
    def __init__(self):
        self.__arquivo = "atendimento.json"
        self.__objetos = []
        self.abrir()