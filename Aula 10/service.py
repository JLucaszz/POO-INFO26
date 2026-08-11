class Service:
    @staticmethod
    def cliente_inserir(id, nome, email, fone, nasc):
        obj = Cliente(id, nome, email, fone, nasc)
        ClienteDAO().inserir(obj)