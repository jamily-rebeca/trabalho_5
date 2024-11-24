import json
from datetime import datetime

class Horario:
    def __init__(self, idHorario, horario):
        self.set_idHorario(idHorario)
        self.set_horario(horario)
        self.set_confirmado(False)
        self.set_idCliente(0)
        self.set_idServico(0)

    def set_idHorario(self, idHorario: int):
        self.__idHorario = idHorario

    def get_idHorario(self):
        return self.__idHorario
    
    def set_horario(self, horario: datetime):
        if horario:
            self.__horario = horario
        else:
            raise ValueError("determine um horário")

    def get_horario_str(self):
        strHorario = datetime.strftime(self.__horario, "%d/%m/%Y %H:%M")
        return strHorario
    
    def get_horario(self):
        return self.__horario

    def set_confirmado(self, confirmado):
      self.__confirmado = confirmado

    def get_confirmado(self):
      return self.__confirmado

    def set_idCliente(self, id_cliente):
      self.__idCliente = id_cliente

    def get_idCliente(self):
      return self.__idCliente

    def set_idServico(self, id_servico):
       self.__idServico = id_servico

    def get_idServico(self):
      return self.__idServico


    def __str__(self):
        return f"{self.get_idHorario()} - {self.get_horario_str()}"
    def to_json(self):
      dic = {}
      dic["id"] = self.get_idHorario()
      dic["data"] = self.get_horario().strftime("%d/%m/%Y %H:%M")
      dic["confirmado"] = self.get_confirmado()
      dic["id_cliente"] = self.get_idCliente()
      dic["id_servico"] = self.get_idServico()
      return dic    

class Horarios:
  objeto: list[Horario] = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.get_idHorario() > m: 
        m = c.get_idHorario()
    obj.set_idHorario(m + 1)
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.get_idHorario() == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.set_horario(obj.get_horario())
      c.set_confirmado(obj.get_confirmado())
      c.set_idCliente(obj.get_idCliente())
      c.set_idServico(obj.get_idServico())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_idHorario())
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  
  @classmethod
  def salvar(cls):
    with open("horarios.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = Horario.to_json)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("horarios.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Horario(
            obj["id"], 
            datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"))
          c.confirmado = obj["confirmado"]
          c.id_cliente = obj["id_cliente"]
          c.id_servico = obj["id_servico"]
          cls.objetos.append(c)
    except FileNotFoundError:
      pass



