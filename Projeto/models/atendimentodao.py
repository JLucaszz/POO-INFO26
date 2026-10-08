import json

from models.atendimento import Atendimento


class AtendimentoDAO:
    def __init__(self):
        self.__arquivo = "atendimentos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        proximo_id = max((atendimento.get_id() for atendimento in self.__objetos), default=0) + 1
        obj.set_id(proximo_id)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        anterior = self.listar_id(obj.get_id())
        if anterior is not None:
            self.__objetos.remove(anterior)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        obj = self.listar_id(id)
        if obj is not None:
            self.__objetos.remove(obj)
            self.__salvar()

    def __abrir(self):
        try:
            with open(self.__arquivo, mode="r", encoding="utf-8") as arquivo:
                atendimentos = json.load(arquivo)
        except FileNotFoundError:
            return

        self.__objetos = [Atendimento.from_json(item) for item in atendimentos]

    def __salvar(self):
        with open(self.__arquivo, mode="w", encoding="utf-8") as arquivo:
            json.dump(
                self.__objetos,
                arquivo,
                default=Atendimento.to_json,
                ensure_ascii=False,
                indent=2,
            )
