import streamlit as st # type: ignore
import pandas as pd # type: ignore
from views import View
import time

class AbrirContaUI:
    @staticmethod
    def main():
        st.header("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Cadastrar"):
            valido = True
            if not nome or not email or not fone or not senha:
                st.warning("Adicione Todos Os Valores.")
            else:
                for p in View.cliente_listar():
                    if p.get_email() == email:
                        st.warning("Esse email já é usado por outro usuário.")
                        valido = False
                        
                if valido:
                    View.cliente_inserir(nome, email, fone, senha)
                    st.success("Paciente cadastrado.")
