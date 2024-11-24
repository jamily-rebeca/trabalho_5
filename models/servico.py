import json
from datetime import timedelta

# Modelo
class Servico:
  def __init__(self, idServico, descricao, valor, duracao):
    self.set_idServico(idServico)
    self.set_descricao(descricao)
    self.set_valor(valor)
    self.set_duracao(duracao)


  def set_idServico(self, idServico: int):
    self.__idServico = idServico

  def get_idServico(self):
    return self.__idServico

  def set_descricao(self, descricao: str):
    if descricao:
      self.__descricao = descricao
    else:
      raise ValueError("determine uma descrição")

  def get_descricao(self):
    return self.__descricao

  def set_duracao(self, duracao:timedelta):
    if duracao:
      self.__duracao = duracao
    else:
      raise ValueError("informe uma duração válida")
        
  def get_duracao(self):
    return self.__duracao
  
  def set_valor(self, valor):
    if valor and valor > 0:
      self.__valor = valor
    else:
      raise ValueError("Adicione um valor válido")

  def get_valor(self):
    return self.__valor

  def __str__(self):
    return f"{self.get_idServico()} - {self.get_descricao()} - R$ {self.get_valor()} - {self.get_duracao()} min"

# Persistência
class Servicos:
  objetos: list[Servico] = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.get_idServico() > m: m = c.get_idServico()
    obj.set_idServico(m + 1)
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.get_idServico() == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.set_descricao(obj.get_descricao())
      c.set_valor(obj.get_valor())
      c.set_duracao(obj.get_duracao())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.get_idServico())
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos

  @classmethod
  def salvar(cls):
    servico = []

    for s in cls.objetos:
      servico.append(
        {
          "id": s.get_idServico(),
          "descricao": s.get_descricao(),
          "valor": s.get_valor(),
          "duracao": s.get_duracao(),
        }
      )
    with open("servicos.json", mode="w") as arquivo:   # w - write
      json.dump(servico, arquivo)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("servicos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

