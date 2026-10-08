from datetime import datetime

class Atendimento:
    def __init__(self, id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario, servicos=None, pago=False):
        self.set_id(id)
        self.set_data(data)
        self.set_queixa_principal(queixa_principal)
        self.set_historico_saude(historico_saude)
        self.set_avaliacao(avaliacao)
        self.set_prescricao(prescricao)
        self.set_id_horario(id_horario)
        self.__servicos = servicos if servicos is not None else []
        self.__pago = pago

    def set_id(self, id):
        if id < 0: raise ValueError("ID inválido")
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_queixa_principal(self, queixa_principal):
        if not queixa_principal: raise ValueError("Queixa principal obrigatória")
        self.__queixa_principal = queixa_principal

    def set_historico_saude(self, historico_saude):
        if not historico_saude: raise ValueError("Histórico de saúde obrigatório")
        self.__historico_saude = historico_saude

    def set_avaliacao(self, avaliacao):
        if not avaliacao: raise ValueError("Avaliação obrigatória")
        self.__avaliacao = avaliacao

    def set_prescricao(self, prescricao):
        if not prescricao: raise ValueError("Prescrição obrigatória")
        self.__prescricao = prescricao

    def set_id_horario(self, id_horario):
        if id_horario < 0: raise ValueError("ID de horário inválido")
        self.__id_horario = id_horario

    def set_pago(self, pago):
        self.__pago = bool(pago)

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_queixa_principal(self): return self.__queixa_principal
    def get_historico_saude(self): return self.__historico_saude
    def get_avaliacao(self): return self.__avaliacao
    def get_prescricao(self): return self.__prescricao
    def get_id_horario(self): return self.__id_horario
    def get_servicos(self): return self.__servicos
    def is_pago(self): return self.__pago

    def calcular_total(self):
        return sum(s.get("valor", 0) if isinstance(s, dict) else s.get_valor() for s in self.__servicos)

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.isoformat() if isinstance(self.__data, datetime) else self.__data,
            "queixa_principal": self.__queixa_principal,
            "historico_saude": self.__historico_saude,
            "avaliacao": self.__avaliacao,
            "prescricao": self.__prescricao,
            "id_horario": self.__id_horario,
            "servicos": self.__servicos,
            "pago": self.__pago
        }

    @staticmethod
    def from_json(dic):
        data_atendimento = datetime.fromisoformat(dic["data"]) if isinstance(dic["data"], str) else dic["data"]
        return Atendimento(
            dic["id"],
            data_atendimento,
            dic["queixa_principal"],
            dic["historico_saude"],
            dic["avaliacao"],
            dic["prescricao"],
            dic["id_horario"],
            dic.get("servicos", []),
            dic.get("pago", False)
        )