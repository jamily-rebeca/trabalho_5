import streamlit as st # type: ignore
import pandas as pd # type: ignore
from views import View
import time

class ManterServicoUI:

    @staticmethod
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()

    @staticmethod
    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0: 
            st.write("Nenhum serviço cadastrado")
        else:    
            #for obj in Servicos: st.write(obj)
            dic = []
            for obj in servicos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        descricao = st.text_input("Informe o nome do serviço")
        valor = st.text_input("Informe o valor (R$)")
        duracao = st.text_input("Informe a duração (minutos)")
        if st.button("Inserir"):
            View.servico_inserir(descricao, float(valor), int(duracao))
            st.success("Servico inserido com sucesso")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0: 
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Atualização de serviço", servicos)
            descricao = st.text_input("Informe o novo nome do serviço", op.descricao)
            valor = st.text_input("Informe o novo valor (R$)", op.valor)
            duracao = st.text_input("Informe a nova duração (minutos)", str(op.duracao))
            if st.button("Atualizar"):
                View.servico_atualizar(op.get_idServico(), descricao, float(valor), int(duracao))
                st.success("Serviço atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0: 
            st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de serviço", servicos)
            if st.button("Excluir"):
                for horarios in View.horario_listar():
                    if op.get_idServico() == horarios.get_idServico():
                        st.warning("Serviço com horário já agendado")
                    else:
                        View.servico_excluir(op.get_idServico())
                        st.success("Serviço excluído com sucesso")
                        st.rerun()
