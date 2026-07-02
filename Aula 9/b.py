from enum import Enum
from datetime import datetime
import json

class Grupo(Enum):
    A = 1
    B = 2
    c = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10
    K = 11
    L = 12

class Fase(Enum):
    GRUPOS = "Fase de Grupos"
    OITAVAS = "Oitavas de Final"
    QUARTAS = "Quartas de Final"
    SEMIFINAL = "Semifinal"
    TERCEIRO = "Disputa do 3º Lugar"
    FINAL = "Final"


class Pais:
    def __init__(self,id, nome, sigla, grupo):
        self.set_id(id)
        self.set_nome(nome)
        self.set_sigla(sigla)
        self.set_grupo(grupo)


    def set_id(self, id):
        if id <= 0: raise ValueError("")
        self.__id = id
    
    def set_nome(self, nome):
        if nome == '': raise ValueError("")
        self.__nome = nome
    
    def set_sigla(self, sigla):
        if len(sigla) != 3: raise ValueError("")
        self.__sigla = sigla.upper

    def set_grupo(self, grupo):
        if not isinstance(grupo, Grupo): raise ValueError("")
        self.__grupo = grupo
    
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_sigla(self): return self.__sigla
    def get_grupo(self): return self.__grupo

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__sigla} - {self.__grupo}"

class Jogo:
    def __init__(self,id, id_pais, id_pais2, gols1, gols2, fase, data_hora):
        self.set_id(id)
        self.set_id_pais(id_pais)
        self.set_id_pais2(id_pais2)
        self.set_gols1(gols1)
        self.set_gols2(gols2)
        self.set_fase(fase)
        self.set_data_hora(data_hora)

class Jogo:
    def __init__(self, id, id_pais, id_pais2, gols1, gols2, fase, data_hora):
        self.set_id(id)
        self.set_id_pais(id_pais)
        self.set_id_pais2(id_pais2)
        self.set_gols1(gols1)
        self.set_gols2(gols2)
        self.set_fase(fase)
        self.set_data_hora(data_hora)

    def set_id(self, id):
        if id <= 0:
            raise ValueError("")
        self.__id = id

    def set_id_pais(self, id_pais):
        if not isinstance(id_pais, Pais):
            raise ValueError("")
        self.__id_pais = id_pais

    def set_id_pais2(self, id_pais2):
        if not isinstance(id_pais2, Pais):
            raise ValueError("")
        self.__id_pais2 = id_pais2

    def set_gols1(self, gols1):
        if gols1 < 0:
            raise ValueError("")
        self.__gols1 = gols1

    def set_gols2(self, gols2):
        if gols2 < 0:
            raise ValueError("")
        self.__gols2 = gols2

    def set_fase(self, fase):
        if not isinstance(fase, Fase):
            raise ValueError("")
        self.__fase = fase

    def set_data_hora(self, data_hora):
        if not isinstance(data_hora, datetime):
            raise ValueError("")
        self.__data_hora = data_hora

    def get_id(self): return self.__id
    def get_id_pais1(self): return self.__id_pais1
    def get_id_pais2(self): return self.__id_pais2
    def get_gols1(self): return self.__gols1
    def get_gols2(self): return self.__gols2
    def get_fase(self): return self.__fase
    def get_data_hora(self): return self.__data_hora