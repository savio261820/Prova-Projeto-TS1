class Ativo:

	def __init__(self, id=None, nome="", tipo="", local="", ultimo_usuario=""):

		self.id = id
		self.nome = nome
		self.tipo = tipo
		self.local = local
		self.ultimo_usuario = ultimo_usuario


class Vulnerabilidade:

	def __init__(self, id=None, ativo_id=0, descricao="", categoria="", severidade="", status="", usuario=""):

		self.id = id
		self.ativo_id = ativo_id
		self.descricao = descricao
		self.categoria = categoria
		self.severidade = severidade
		self.status = status
		self.usuario = usuario
