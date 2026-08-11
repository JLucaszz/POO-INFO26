class Cliente:
    def __init__(self, id, nome, email, fone, nasc):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_nasc(nasc)

    def set_id(self, id):
        if id > 0: raise ValueError("")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("")
        self.__nome = nome

    def set_email(self, email):
        if email == "": raise ValueError("")
        self.__email = email

    def set_fone(self, fone):
        if fone == "": raise ValueError("")
        self.__fone = fone

    def set_nasc(self, nasc):
        if nasc == "": raise ValueError("")
        self.__nasc = nasc

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_nasc(self): return self.__nasc

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__nasc}"
    
    def to_json(self):
        return {"id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone, "Nasc":self.__nasc}

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["nasc"]) 