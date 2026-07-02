from models.clientes import Clientes
from models.clientedao import ClientesDAO

class Service:
    @staticmethod
    def clientes_inserir(id, nome, email, fone):
        obj = Clientes(id, nome, email, fone)
        ClientesDAO().inserir(obj)

    @staticmethod
    def clientes_listar():
        return ClientesDAO().listar()
    
    @staticmethod
    def clientes_listar_id(id):
        return ClientesDAO().listar_id(id)
    
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Clientes(id, nome, email, fone)
        ClientesDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClientesDAO().excluir(id)


