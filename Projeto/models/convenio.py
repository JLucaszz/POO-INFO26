class Convenio:
    def __init__(self, id, nome, fone, contato):
        self.set_id(id)
        self.set_nome(nome)
        self.set_fone(fone)
        self.set_contato(contato)

    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id

    def set_nome(self, nome):
        if nome == '': raise ValueError()
        self.__nome = nome

    def sett_fone(self, fone):
        if fone == '': raise ValueError()
        self.__fone = fone

    def set_contato(self, contato):
        if contato == '': raise ValueError()
        self.__contato = contato

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_fone(self): return self.__fone
    def get_contato(self): return self.__contato

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__fone} - {self.__contato}"

    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "fone":self.__fone, "contato":self.__contato}
        return dic

    def from_json(dic):
        Convenio = Convenio(dic["id"], dic["nome"], dic["fone"], dic["contato"])
        return Convenio
