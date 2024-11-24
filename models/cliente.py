# Lista de Clientes
# C - Create - Insere um objeto na lista
# R - Read   - Listar os objetos da lista
# U - Update - Atualizar um objeto na lista
# D - Delete - Exclui um objeto da lista

import json

# Modelo
class Cliente:
  def __init__(self, idCliente, nome, email, fone, senha):
    self.set_idCliente(idCliente)
    self.set_nome(nome)
    self.set_email(email)
    self.set_fone(fone)
    self.set_senha(senha)



  def set_idCliente(self, idCliente: int):
    self.__idCliente = idCliente

  def get_idCliente(self):
    return self.__idCliente

  def set_nome(self, nome: str):
    if nome:
      self.__nome = nome
    else:
      raise ValueError("informe o nome do cliente")

  def get_nome(self):
    return self.__nome

  def set_fone(self, fone: str):
    if fone:
      self.__fone = fone
    else:
      raise ValueError("Adicione o telefone")

  def get_fone(self):
    return self.__fone


  def set_senha(self, senha):
    if senha:
      self.__senha = senha
    else:
      raise ValueError("Informe a senha que desejas utilizar")

  def get_senha(self):
    return self.__senha

  def set_email(self, email):
    if email:
      self.__email = email
    else:
      raise ValueError("Informe um email")

  def get_email(self):
    return self.__email



  def __str__(self):
    return f"{self.get_nome()} - {self.get_email()} - {self.get_fone()} - {self.get_idCliente()}"

# Persistência
class Clientes:
  objetos = []    # atributo estático

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for c in cls.objetos:
      if c.id > m: m = c.id
    obj.id = m + 1
    cls.objetos.append(obj)
    cls.salvar()

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None  
  
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      c.nome = obj.nome
      c.email = obj.email
      c.fone = obj.fone
      c.senha = obj.senha
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
      cls.objetos.remove(c)
      cls.salvar()
  
  @classmethod
  def listar(cls):
    cls.abrir()
    cls.objetos.sort(key=lambda cliente: cliente.nome)
    return cls.objetos

  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("clientes.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

