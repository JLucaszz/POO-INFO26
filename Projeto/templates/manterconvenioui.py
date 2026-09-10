import streamlit as st
import pandas as pd
import time
from service import Service

class ManterConvenioUI:
    def main():
        st.header("Cadastro de Convenio")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterConvenioUI.listar()
        with tab2: ManterConvenioUI.inserir()
        with tab3: ManterConvenioUI.atualizar()
        with tab4: ManterConvenioUI.excluir()
    def listar():
        convenio = Service.convenio_listar()
        if len(convenio) == 0: st.write("Nenhum convenio cadastrado")
        else:
            list_dic = []
            for obj in convenio: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome = st.text_input("Informe o nome")
        fone = st.text_input("Informe o fone")
        contato = st.text_input("Informe o  contato")
        if st.button("Inserir"):
            Service.convenio_inserir(nome, fone, contato)
            st.success("Convenio inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        convenio = Service.convenio_listar()
        if len(convenio) == 0: st.write("Nenhum convenio cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", convenio)
            nome = st.text_input("Novo nome", op.get_nome())
            fone = st.text_input("Novo fone", op.get_fone())
            contato = st.text_input("Novo contato", op.get_contato())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.convenio_atualizar(id, nome, fone, contato)
                st.success("Convenio atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        convenio = Service.convenio_listar()
        if len(convenio) == 0: st.write("Nenhum convenio cadastrado")
        else:
            op = st.selectbox("Exclusão de Convenio", convenio)
            if st.button("Excluir"):
              id = op.get_id()
              Service.convenio_excluir(id)
              st.success("Convenio excluído com sucesso")
              time.sleep(2)
              st.rerun()
