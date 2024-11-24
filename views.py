from models.cliente import Cliente, Clientes
from models.horario import Horario, Horarios
from models.servico import Servico, Servicos
from datetime import datetime, timedelta

class View:
    @staticmethod
    def cliente_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(c)

    @staticmethod
    def cliente_listar():
        return Clientes.listar()    

    @staticmethod
    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)    

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_idCliente(), "nome" : c.get_nome() }
        return None

    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_idCliente(id_cliente)
        c.set_idServico(id_servico)
        Horarios.inserir(c)

    @staticmethod
    def horario_listar():
        return Horarios.listar()    

    @staticmethod
    def horario_listar_disponiveis():
        horarios = View.horario_listar()
        disponiveis = []
        for h in horarios:
            if h.data >= datetime.now() and h.get_idCliente() == None: disponiveis.append(h)
        return disponiveis   

    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_idCliente(id_cliente)
        c.set_idServico(id_servico)
        Horarios.atualizar(c)

    @staticmethod
    def horario_excluir(id):
        c = Horario(id, None)
        Horarios.excluir(c)    

    @staticmethod
    def horario_abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        #data = "05/11/2024"
        #inicio = "08:00"
        #fim = "12:00"
        #intervalo = 60
        i = data + " " + hora_inicio   # "05/11/2024 08:00"
        f = data + " " + hora_fim      # "05/11/2024 12:00"
        d = timedelta(minutes=intervalo)
        di = datetime.strptime(i, "%d/%m/%Y %H:%M")
        df = datetime.strptime(f, "%d/%m/%Y %H:%M")
        x = di
        while x <= df:
            #cadastrar o horário x
            View.horario_inserir(x, False, None, None)
            #passar para o próximo horário
            x = x + d

    @staticmethod
    def servico_inserir(descricao, valor, duracao):
        c = Servico(0, descricao, valor, duracao)
        Servicos.inserir(c)

    @staticmethod
    def servico_listar():
        return Servicos.listar()    

    @staticmethod
    def servico_listar_id(id):
        return Servicos.listar_id(id)    

    @staticmethod
    def servico_atualizar(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.atualizar(c)

    @staticmethod
    def servico_excluir(id, descricao, valor, duracao):
        c = Servico(id, descricao, valor, duracao)
        Servicos.excluir(c)    
