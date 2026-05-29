from database.connection import conectar

severidades = [
	"Baixa",
	"Média",
	"Alta",
	"Crítica"
]

status_lista = [
	"Aberta",
	"Em tratamento",
	"Corrigida",
	"Aceita como risco"
]

def cadastrar_vulnerabilidade():

	conexao = conectar()
	cursor = conexao.cursor()
	cursor.execute("""

	SELECT
		id,
		nome

	FROM ativos

	ORDER BY id

	""")

	ativos = cursor.fetchall()

	if len(ativos) == 0:

		print("\nNenhum ativo cadastrado.")

		conexao.close()

		return

	print("\nATIVOS:\n")

	ativos_dict = {}

	for ativo in ativos:

		ativos_dict[ativo[0]] = ativo[1]

		print(
			"ID:",
			ativo[0],
			"-",
			ativo[1]
		)

	print("\nDigite 0 para cancelar.")

	while True:

		entrada = input(
			"\nDigite o ID do ativo: "
		).strip()

		if entrada == "0":

			print("\nOperação cancelada.")

			conexao.close()

			return

		if not entrada.isdigit():

			print("\nDigite apenas números.")

			continue

		ativo_id = int(entrada)

		if ativo_id in ativos_dict:
			break

		print("\nID inválido.")

	while True:

		descricao = input("Descrição da vulnerabilidade: ").strip()

		if descricao.lower() == "0":

			print("\nOperação cancelada.")

			conexao.close()

			return

		if descricao != "":
			break

		print("Descrição inválida.")

	while True:

		categoria = input("Categoria/Tipo: ").strip()

		if categoria.lower() == "0":

			print("\nOperação cancelada.")

			conexao.close()

			return

		if categoria != "":
			break

		print("Categoria inválida.")

	print("\nSeveridades:\n")

	for i, valor in enumerate(severidades, start=1):

		print(i, "-", valor)

	print("0 - Cancelar")

	while True:

		entrada = input("Escolha a severidade: ").strip()

		if entrada == "0":

			print("\nOperação cancelada.")

			conexao.close()

			return

		if not entrada.isdigit():

			print("\nDigite apenas números.")

			continue

		escolha = int(entrada)

		if escolha in [1,2,3,4]:

			severidade = severidades[
				escolha - 1
			]

			break

		print("Opção inválida.")

	# STATUS
	print("\nStatus:\n")

	for i, valor in enumerate(status_lista, start=1):

		print(i, "-", valor)

	print("0 - Cancelar")

	while True:

		entrada = input("Escolha o status: ").strip()

		if entrada == "0":

			print("\nOperação cancelada.")

			conexao.close()

			return

		if not entrada.isdigit():

			print("\nDigite apenas números.")

			continue

		escolha = int(entrada)

		if escolha in [1,2,3,4]:

			status = status_lista[
				escolha - 1
			]

			break

		print("Opção inválida.")

	while True:

		usuario = input("Seu nome: ").strip()

		if usuario == "0":

			print("\nOperação cancelada.")

			conexao.close()

			return

		if usuario != "":
			break

		print("Nome inválido.")

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
		ativo_id,
		descricao,
		categoria,
		severidade,
		status,
		usuario
	))

	conexao.commit()

	print("\nVulnerabilidade cadastrada com sucesso.")

	conexao.close()