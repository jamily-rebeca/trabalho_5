import streamlit as st # type: ignore
from views import View
from datetime import datetime
import time

class AbrirAgendaUI:
    @staticmethod
    def main():
        st.header("Abrir Agenda do Dia")
        AbrirAgendaUI.abrir_agenda()

    @staticmethod
    def abrir_agenda():
        data = st.date_input("Qual o dia que desejas abrir a agenda?")
        Hinicial = st.time_input("Qual o horário inicial pra as consultas?")
        Hfinal = st.time_input("Qual horário final para as consultas?")
        intervalo = st.time_input("Qual o intervalo entre as consultas?")

        if st.button("Criar"):
            View.horario_abrir_agenda(data, Hinicial, Hfinal, intervalo)
            st.success("Agenda Criada")
            time.sleep(2)
            st.rerun()

