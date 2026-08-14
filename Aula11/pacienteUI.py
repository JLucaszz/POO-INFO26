import streamlit as st
from paciente import Paciente


class PacienteUI:
    def main():
        st.header("Dados do Paciente")
        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        telefone = st.text_input("Telefone")
        nascimento = st.date_input("Data de Nascimento")

        if st.button("Idade"):
            paciente = Paciente(nome, cpf, telefone, nascimento)
            st.write(str(paciente))
            st.success(f"Idade: {paciente.idade()}")
