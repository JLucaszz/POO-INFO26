import streamlit as st
from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento

    def __str__(self):
        return f"Nome = {self.__nome}, CPF = {self.__cpf}, Telefone = {self.__telefone}, Nascimento {self.__nascimento}"
    def idade(self):
        return datetime.now - self.__nascimento