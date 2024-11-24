import streamlit as st # type: ignore
from views import View
import time

class LoginUI:

    @staticmethod
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            if c == None: st.write("E-mail ou senha inválidos")
            else:
                st.session_state["cliente_id"] = c["id"]
                st.session_state["nome"] = c["nome"]
                st.rerun()





                #VERIFICA SE O CLIENTE EXISTE E PASSA OS DADOS PARA O SESSION STATE