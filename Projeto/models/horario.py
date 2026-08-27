from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(False)
        self.set_id_clientes(0)
        self.set_id_servico(0)

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y  %H:%M' )} - {self.__confirmado}"

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_clientes(self): return self.__id_clientes
    def get_id_servico(self): return self.__id_servico

    def set_id(self, id):
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado

    def set_id_clientes(self, id_clientes):
        self.__id_clientes = id_clientes

    def set_id_servico(self, id_servico):
        self.__id_servico = id_servico

    def to_json(self):
        dic = {"id": self.__id, "data":self.__data.strftime("%d/%m/%Y %H:%M"), "confirmado":self.__confirmado, "id_clientes":self.__id_clientes, "id_servico":self.__id_servico}
        return dic

    @staticmethod
    def from_json(dic):
        horario = horario(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
        horario.set_confirmado(dic["confirmado"])
        horario.set_id_clientes(dic["id_clientes"])
        horario.set_id_servico(dic["id_servico"])
        return horario

    
