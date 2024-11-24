import streamlit as st # type: ignore
import pandas as pd # type: ignore
from views import View
import time
from datetime import datetime

class ManterHorarioUI:

    @staticmethod
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    @staticmethod
    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:  
            dic = []
            #for obj in Horarios: dic.append(obj.__dict__)

            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_idCliente())
                servico = View.servico_listar_id(obj.get_idServico())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                dic.append({"id" : obj.get_idHorario(), "data" : obj.get_horario(), "confirmado" : obj.get_confirmado(), "cliente" : cliente, "serviço" : servico})
            
            df = pd.DataFrame(dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        data = st.text_input("Informe a data e horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente", clientes, index = None)
        servico = st.selectbox("Informe o serviço", servicos, index = None)
        if st.button("Inserir"):
            id_cliente = None
            id_servico = None
            if cliente != None:
                id_cliente = cliente.get_idCliente()
            if servico != None:
                id_servico = servico.get_idServico()
            servicos = View.servico_listar()
            clientes =  View.cliente_listar()
            for x in servicos:
                if id_servico == x.get_idServico():
                    for y in clientes:
                        if id_cliente == y.get_idCliente():
                            View.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico)
                            st.success("Horário inserido com sucesso")
                            time.sleep(2)
                            st.rerun()
            st.warning("Serviço ou cliente inexistente")

    @staticmethod        
    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:
            clientes = View.cliente_listar()
            servicos = View.servico_listar()
            op = st.selectbox("Atualização de horário", horarios)
            data = st.text_input("Informe a nova data e horário do serviço", op.get_horario())
            confirmado = st.checkbox("Nova confirmação", op.get_confirmado())
            id_cliente = None if op.get_idCliente() in [0, None] else op.get_idCliente()
            id_servico = None if op.get_idServico() in [0, None] else op.get_idServico()
            cliente = st.selectbox("Informe o novo cliente", clientes, next((i for i, c in enumerate(clientes) if c.get_idCliente() == id_cliente), None))
            servico = st.selectbox("Informe o novo serviço", servicos, next((i for i, s in enumerate(servicos) if s.get_idServico() == id_servico), None))
            if st.button("Atualizar"):
                id_cliente = None
                id_servico = None
                if cliente != None: 
                    id_cliente = cliente.get_idCliente()
                if servico != None: 
                    id_servico = servico.get_idServico()
                servicos = View.servico_listar()
                clientes =  View.cliente_listar()
                for x in servicos:
                    if id_servico == x.get_idServico():
                        for y in clientes:
                            if id_cliente == y.get_idCliente():
                                View.horario_atualizar(op.id, datetime.strptime(data, "%d/%m/%Y %H:%M"),  confirmado, id_cliente, id_servico)
                                st.success("Horário atualizado com sucesso")
                                time.sleep(2)
                                st.rerun()

    @staticmethod
    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de horário", horarios)
            if st.button("Excluir"):
                if op.get_idCliente() == 0:
                    View.horario_excluir(op.get_horario())
                    st.success("Horário excluído com sucesso")
                    time.sleep(2)
                    st.rerun()

                else:
                    st.warning("Horário já preenchido")
