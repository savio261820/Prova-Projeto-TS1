from src.modelo import Ativo, Vulnerabilidade


class AtivoRepositorio:

	def __init__(self, database):

		self.database = database

	def listar_todos(self):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		SELECT
			id,
			nome,
			tipo,
			local,
			ultimo_usuario

		FROM ativos

		""")

		ativos = cursor.fetchall()

		return [Ativo(*t) for t in ativos]

	def listar_ids_nomes(self):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		SELECT
			id,
			nome

		FROM ativos

		ORDER BY id

		""")

		return cursor.fetchall()

	def buscar_por_id(self, id):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		SELECT
			id,
			nome,
			tipo,
			local,
			ultimo_usuario

		FROM ativos

		WHERE id = ?

		""", (id,))

		ativo = cursor.fetchone()

		if ativo:
			return Ativo(*ativo)

		return None

	def buscar_por_nome(self, nome):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		SELECT
			id,
			nome,
			tipo,
			local,
			ultimo_usuario

		FROM ativos

		WHERE LOWER(nome) = LOWER(?)

		""", (nome,))

		ativos = cursor.fetchall()

		return [Ativo(*t) for t in ativos]

	def buscar_por_usuario(self, usuario):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		SELECT
			id,
			nome,
			tipo,
			local,
			ultimo_usuario

		FROM ativos

		WHERE LOWER(ultimo_usuario) = LOWER(?)

		""", (usuario,))

		ativos = cursor.fetchall()

		return [Ativo(*t) for t in ativos]

	def buscar_por_local(self, local):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		SELECT
			id,
			nome,
			tipo,
			local,
			ultimo_usuario

		FROM ativos

		WHERE LOWER(local) = LOWER(?)

		""", (local,))

		ativos = cursor.fetchall()

		return [Ativo(*t) for t in ativos]

	def salvar(self, ativo):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		INSERT INTO ativos (
			nome,
			tipo,
			local,
			ultimo_usuario
		)

		VALUES (?, ?, ?, ?)

		""", (
			ativo.nome,
			ativo.tipo,
			ativo.local,
			ativo.ultimo_usuario
		))

		conexao.commit()

		return cursor.lastrowid

	def atualizar(self, ativo):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		UPDATE ativos

		SET
			nome = ?,
			tipo = ?,
			local = ?,
			ultimo_usuario = ?

		WHERE id = ?

		""", (
			ativo.nome,
			ativo.tipo,
			ativo.local,
			ativo.ultimo_usuario,
			ativo.id
		))

		conexao.commit()

	def deletar(self, id):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		DELETE FROM ativos

		WHERE id = ?

		""", (id,))

		conexao.commit()

	def listar_ids_disponiveis(self):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		SELECT DISTINCT id

		FROM ativos

		""")

		return [t[0] for t in cursor.fetchall()]

	def listar_nomes_disponiveis(self):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		SELECT DISTINCT nome

		FROM ativos

		ORDER BY nome

		""")

		return [t[0] for t in cursor.fetchall()]

	def listar_usuarios_disponiveis(self):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		SELECT DISTINCT ultimo_usuario

		FROM ativos

		ORDER BY ultimo_usuario

		""")

		return [t[0] for t in cursor.fetchall()]

	def listar_locais_disponiveis(self):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		SELECT DISTINCT local

		FROM ativos

		ORDER BY local

		""")

		return [t[0] for t in cursor.fetchall()]


class VulnerabilidadeRepositorio:

	def __init__(self, database):

		self.database = database

	def listar_por_ativo_id(self, ativo_id):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		SELECT
			descricao,
			severidade,
			status

		FROM vulnerabilidades

		WHERE ativo_id = ?

		""", (ativo_id,))

		return cursor.fetchall()

	def salvar(self, vuln):

		conexao = self.database.conectar()
		cursor = conexao.cursor()

		cursor.execute("""

		INSERT INTO vulnerabilidades (

			ativo_id,
			descricao,
			categoria,
			severidade,
			status,
			usuario

		)

		VALUES (?, ?, ?, ?, ?, ?)

		""", (
			vuln.ativo_id,
			vuln.descricao,
			vuln.categoria,
			vuln.severidade,
			vuln.status,
			vuln.usuario
		))

		conexao.commit()

		return cursor.lastrowid
