import time
from datetime import datetime

import pandas as pd
import streamlit as st

from service import Service


class ManterAtendimentoUI:
    def main():
        st.header("Atendimentos")
        profissional = st.session_state.get("usuario_tipo") == "profissional"
        administrador = st.session_state.get("usuario_nome") == "admin"

        if profissional:
            tab1, tab2 = st.tabs(["Meus atendimentos", "Registrar atendimento"])
            with tab1:
                ManterAtendimentoUI.listar()
            with tab2:
                ManterAtendimentoUI.inserir()
        elif administrador:
            tab1, tab2, tab3, tab4 = st.tabs(
                ["Listar", "Inserir", "Atualizar", "Excluir"]
            )
            with tab1:
                ManterAtendimentoUI.listar()
            with tab2:
                ManterAtendimentoUI.inserir()
            with tab3:
                ManterAtendimentoUI.atualizar()
            with tab4:
                ManterAtendimentoUI.excluir()
        else:
            st.error("Apenas profissionais podem acessar os atendimentos.")

    def listar():
        if st.session_state.get("usuario_tipo") == "profissional":
            atendimentos = Service.atendimento_listar_profissional(
                st.session_state["usuario_id"]
            )
        else:
            atendimentos = Service.atendimento_listar()

        if not atendimentos:
            st.write("Nenhum atendimento cadastrado")
            return

        registros = []
        for atendimento in atendimentos:
            horario = Service.horario_listar_id(atendimento.get_id_horario())
            cliente = (
                Service.cliente_listar_id(horario.get_id_cliente())
                if horario is not None
                else None
            )
            registros.append(
                {
                    "id": atendimento.get_id(),
                    "data": atendimento.get_data().strftime("%d/%m/%Y %H:%M"),
                    "cliente": cliente.get_nome() if cliente is not None else "—",
                    "queixa principal": atendimento.get_queixa_principal(),
                    "histórico de saúde": atendimento.get_historico_saude(),
                    "avaliação clínica": atendimento.get_avaliacao(),
                    "prescrição de exames e medicamentos": atendimento.get_prescricao(),
                    "serviços realizados": ", ".join(
                        servico["descricao"] for servico in atendimento.get_servicos()
                    ),
                    "total (R$)": atendimento.get_valor_total(),
                }
            )
        st.dataframe(pd.DataFrame(registros), use_container_width=True)

    def inserir():
        if st.session_state.get("usuario_tipo") == "profissional":
            id_profissional = st.session_state["usuario_id"]
            horarios = Service.atendimento_horarios_pendentes(id_profissional)
        else:
            horarios = Service.atendimento_horarios_pendentes()

        if not horarios:
            st.write("Não há horários agendados sem atendimento registrado.")
            return

        servicos_disponiveis = Service.servico_listar()
        if not servicos_disponiveis:
            st.write("Cadastre serviços antes de registrar um atendimento.")
            return

        nomes_clientes = {}
        for horario_agendado in horarios:
            cliente = Service.cliente_listar_id(horario_agendado.get_id_cliente())
            nomes_clientes[horario_agendado.get_id()] = (
                cliente.get_nome() if cliente is not None else "Cliente não encontrado"
            )

        horario = st.selectbox(
            "Cliente e horário agendado",
            horarios,
            format_func=lambda item: (
                f"{nomes_clientes[item.get_id()]} — "
                f"{item.get_data().strftime('%d/%m/%Y %H:%M')}"
            ),
        )
        data = st.text_input(
            "Data e horário do atendimento (dd/mm/aaaa HH:MM)",
            horario.get_data().strftime("%d/%m/%Y %H:%M"),
        )
        queixa_principal = st.text_area("Queixa principal")
        historico_saude = st.text_area("Histórico de saúde")
        avaliacao = st.text_area("Avaliação clínica")
        prescricao = st.text_area(
            "Prescrição de exames e medicamentos",
            help="Registre os exames solicitados e os medicamentos prescritos.",
        )

        servico_agendado = next(
            (
                servico
                for servico in servicos_disponiveis
                if servico.get_id() == horario.get_id_servico()
            ),
            None,
        )
        servicos_padrao = (
            [servico_agendado]
            if servico_agendado in servicos_disponiveis
            else []
        )
        servicos = st.multiselect(
            "Serviços ou procedimentos realizados",
            servicos_disponiveis,
            default=servicos_padrao,
            format_func=lambda servico: (
                f"{servico.get_descricao()} — R$ {servico.get_valor():.2f}"
            ),
        )
        st.caption(
            f"Total dos serviços: R$ "
            f"{round(sum(servico.get_valor() for servico in servicos), 2):.2f}"
        )

        if st.button("Registrar atendimento"):
            try:
                data_atendimento = datetime.strptime(data, "%d/%m/%Y %H:%M")
                profissional_id = (
                    st.session_state["usuario_id"]
                    if st.session_state.get("usuario_tipo") == "profissional"
                    else horario.get_id_profissional()
                )
                Service.atendimento_registrar(
                    profissional_id,
                    horario.get_id(),
                    data_atendimento,
                    queixa_principal,
                    historico_saude,
                    avaliacao,
                    prescricao,
                    [servico.get_id() for servico in servicos],
                )
            except ValueError as erro:
                st.error(str(erro))
            else:
                st.success("Atendimento registrado com sucesso.")
                time.sleep(1)
                st.rerun()

    def atualizar():
        atendimentos = Service.atendimento_listar()
        if not atendimentos:
            st.write("Nenhum atendimento cadastrado")
            return

        atendimento = st.selectbox("Atendimento", atendimentos)
        data = st.text_input(
            "Data e horário do atendimento (dd/mm/aaaa HH:MM)",
            atendimento.get_data().strftime("%d/%m/%Y %H:%M"),
        )
        queixa_principal = st.text_area(
            "Queixa principal", atendimento.get_queixa_principal()
        )
        historico_saude = st.text_area(
            "Histórico de saúde", atendimento.get_historico_saude()
        )
        avaliacao = st.text_area("Avaliação clínica", atendimento.get_avaliacao())
        prescricao = st.text_area(
            "Prescrição de exames e medicamentos", atendimento.get_prescricao()
        )

        if st.button("Atualizar atendimento"):
            try:
                data_atendimento = datetime.strptime(data, "%d/%m/%Y %H:%M")
                Service.atendimento_atualizar(
                    atendimento.get_id(),
                    data_atendimento,
                    queixa_principal,
                    historico_saude,
                    avaliacao,
                    prescricao,
                    atendimento.get_id_horario(),
                )
            except ValueError as erro:
                st.error(str(erro))
            else:
                st.success("Atendimento atualizado com sucesso.")
                time.sleep(1)
                st.rerun()

    def excluir():
        atendimentos = Service.atendimento_listar()
        if not atendimentos:
            st.write("Nenhum atendimento cadastrado")
            return

        atendimento = st.selectbox("Atendimento a excluir", atendimentos)
        if st.button("Excluir atendimento"):
            Service.atendimento_excluir(atendimento.get_id())
            st.success("Atendimento excluído com sucesso.")
            time.sleep(1)
            st.rerun()
