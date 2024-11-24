import streamlit as st # type: ignore
import pandas as pd # type: ignore
from views import View

class ListarHorarioUI:
    @staticmethod
    def main():
        st.header("Horários Disponíveis")
        ListarHorarioUI.listar()

    @staticmethod
    def listar():
        horarios = View.horario_listar_disponiveis()
        if len(horarios) == 0:
            st.write("Nenhum horário disponível")
        else:
            dic = []
            for obj in horarios: dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)
