from models.clientes import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.atendimento import Atendimento
from models.atendimentodao import AtendimentoDAO
from models.profissional import Profissional
from models.profissionaldao import ProfissionalDAO
from datetime import datetime, timedelta

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        obj = Cliente(0, nome, email, fone, senha)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        r = ClienteDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return
        Service.cliente_inserir("admin", "admin", "fone", "1234")        
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Service.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None


    @staticmethod
    def servico_inserir(descricao, valor):
        obj = Servico(0, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        r = ServicoDAO().listar()
        r.sort(key = lambda obj : obj.get_descricao().casefold())
        return r
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
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO().inserir(c)
    @staticmethod
    def horario_listar(): # select - order by
        r = HorarioDAO().listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id) 
    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO().atualizar(c)
    @staticmethod
    def horario_excluir(id):
        HorarioDAO().excluir(id) 
    @staticmethod
    def horario_listar_disponiveis(id_profissional):
        r = []
        agora = datetime.now()
        for h in Service.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False \
            and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort (key = lambda h : h.get_data())
        return r
    @staticmethod
    def horario_abrir_minha_agenda(data, horario_inicio, horario_fim, intervalo, id_profissional):
        data_inicio = datetime.strptime(data + " " + horario_inicio, "%d/%m/%Y %H:%M")
        data_fim = datetime.strptime(data + " " + horario_fim, "%d/%m/%Y %H:%M")
        delta = timedelta(minutes = intervalo)
        x = data_inicio
        while x <= data_fim:
            # inserir um horário
            Service.horario_inserir(x, False, None, None, id_profissional)
            # passar para o horário seguinte
            x = x + delta
    @staticmethod
    def horario_visualizar_minha_agenda(id_profissional):
        r = []
        for h in Service.horario_listar():
            if h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort (key = lambda h : h.get_data())
        return r
    @staticmethod
    def horario_visualizar_meus_servicos(id_cliente): # select - where
        r = []
        for h in Service.horario_listar():
            if h.get_id_cliente() == id_cliente:
                r.append(h)
        r.sort (key = lambda h : h.get_data())
        return r
    @staticmethod
    def horario_confirmar_servico(id_profissional):
        r = []
        for h in Service.horario_listar():
            if h.get_confirmado() == False \
            and h.get_id_cliente() != None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort (key = lambda h : h.get_data())
        return r
       
    @staticmethod
    def atendimento_inserir(
        data,
        queixa_principal,
        historico_saude,
        avaliacao,
        prescricao,
        id_horario,
        servicos=None,
    ):
        obj = Atendimento(
            0,
            data,
            queixa_principal,
            historico_saude,
            avaliacao,
            prescricao,
            id_horario,
            servicos,
        )
        AtendimentoDAO().inserir(obj)

    @staticmethod
    def atendimento_registrar(
        id_profissional,
        id_horario,
        data,
        queixa_principal,
        historico_saude,
        avaliacao,
        prescricao,
        ids_servicos,
    ):
        horario = Service.horario_listar_id(id_horario)
        if (
            horario is None
            or id_profissional is None
            or horario.get_id_profissional() != id_profissional
        ):
            raise ValueError("O horário não pertence à sua agenda")
        if horario.get_id_cliente() in (None, 0):
            raise ValueError("O horário ainda não está agendado por um cliente")
        if any(
            atendimento.get_id_horario() == id_horario
            for atendimento in Service.atendimento_listar()
        ):
            raise ValueError("Esse horário já possui um atendimento registrado")

        servicos = []
        for id_servico in ids_servicos:
            servico = Service.servico_listar_id(id_servico)
            if servico is None:
                raise ValueError("Um dos serviços selecionados não existe mais")
            servicos.append(
                {
                    "id": servico.get_id(),
                    "descricao": servico.get_descricao(),
                    "valor": servico.get_valor(),
                }
            )
        if not servicos:
            raise ValueError("Selecione ao menos um serviço realizado")

        Service.atendimento_inserir(
            data,
            queixa_principal,
            historico_saude,
            avaliacao,
            prescricao,
            id_horario,
            servicos,
        )
        Service.horario_atualizar(
            horario.get_id(),
            horario.get_data(),
            True,
            horario.get_id_cliente(),
            horario.get_id_servico(),
            horario.get_id_profissional(),
        )

    @staticmethod
    def atendimento_listar():
        r = AtendimentoDAO().listar()
        r.sort(key = lambda obj : obj.get_data())
        return r

    @staticmethod
    def atendimento_listar_profissional(id_profissional):
        atendimentos = []
        for atendimento in Service.atendimento_listar():
            horario = Service.horario_listar_id(atendimento.get_id_horario())
            if horario is not None and horario.get_id_profissional() == id_profissional:
                atendimentos.append(atendimento)
        return atendimentos

    @staticmethod
    def atendimento_horarios_pendentes(id_profissional=None):
        horarios_com_atendimento = {
            atendimento.get_id_horario() for atendimento in Service.atendimento_listar()
        }
        return [
            horario
            for horario in Service.horario_listar()
            if horario.get_id_cliente() not in (None, 0)
            and horario.get_id_profissional() not in (None, 0)
            and horario.get_id() not in horarios_com_atendimento
            and (
                id_profissional is None
                or horario.get_id_profissional() == id_profissional
            )
        ]

    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)
    @staticmethod
    def atendimento_atualizar(
        id,
        data,
        queixa_principal,
        historico_saude,
        avaliacao,
        prescricao,
        id_horario,
        servicos=None,
    ):
        anterior = AtendimentoDAO().listar_id(id)
        if servicos is None and anterior is not None:
            servicos = anterior.get_servicos()
        obj = Atendimento(
            id,
            data,
            queixa_principal,
            historico_saude,
            avaliacao,
            prescricao,
            id_horario,
            servicos,
        )
        AtendimentoDAO().atualizar(obj)
    @staticmethod
    def atendimento_excluir(id):
        AtendimentoDAO().excluir(id)


    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        obj = Profissional(0, nome, email, especialidade, senha)
        ProfissionalDAO().inserir(obj)
    @staticmethod
    def profissional_listar():
        r = ProfissionalDAO().listar()
        r.sort(key = lambda obj : obj.get_nome().casefold())
        return r
    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)
    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, senha):
        obj = Profissional(id, nome, email, especialidade, senha)
        ProfissionalDAO().atualizar(obj)
    @staticmethod
    def profissional_excluir(id):
        ProfissionalDAO().excluir(id)
    @staticmethod
    def profissional_autenticar(email, senha):
        for c in Service.profissional_listar():
            if senha and c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None