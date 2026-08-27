from models.clientes import Clientes         # entidade
from models.clientedao import ClienteDAO   # persistência
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario, HorarioDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        obj = Clientes(0, nome, email, fone)
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    
    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Clientes(id, nome, email, fone)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    
    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)

    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()
    
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)

    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)

    @staticmethod
    def horario_inserir(data, confirmado, id_cliestes, id_servico):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_clientes(id_cliestes)
        c.set_id_servico(id_servico)
        HorarioDAO().inserir(c)

    @staticmethod
    def horario_listar():
        return HorarioDAO().listar()

    @staticmethod
    def horario_listar_id(id):