import sqlite3


class Database:

	def __init__(self):

		self.conexao = sqlite3.connect("database/security.db")
		self.conexao.execute("PRAGMA foreign_keys = ON")
		self.criar_tabelas()

	def conectar(self):

		return self.conexao

	def fechar(self):

		self.conexao.close()

	def criar_tabelas(self):

		cursor = self.conexao.cursor()

		cursor.execute("""

		CREATE TABLE IF NOT EXISTS ativos (

			id INTEGER PRIMARY KEY AUTOINCREMENT,

			nome TEXT NOT NULL,

			tipo TEXT NOT NULL,

			local TEXT NOT NULL,

			ultimo_usuario TEXT NOT NULL

		)

		""")

		cursor.execute("""

		CREATE TABLE IF NOT EXISTS vulnerabilidades (

			id INTEGER PRIMARY KEY AUTOINCREMENT,

			ativo_id INTEGER NOT NULL,

			descricao TEXT NOT NULL,

			categoria TEXT NOT NULL,

			severidade TEXT NOT NULL,

			status TEXT NOT NULL,

			usuario TEXT NOT NULL,

			FOREIGN KEY (ativo_id)
			REFERENCES ativos(id)
			ON DELETE CASCADE

		)

		""")

		self.conexao.commit()


def conectar():

	db = Database()
	return db.conectar()
