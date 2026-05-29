from database.connection import conectar

conexao = conectar()

cursor = conexao.cursor()

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

conexao.commit()

conexao.close()

print("Banco criado com sucesso.")