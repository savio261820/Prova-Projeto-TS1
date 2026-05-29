from database.connection import conectar

def listar_vulnerabilidades():

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

	for ativo in ativos:

		print(
			"ID:",
			ativo[0],
			"-",
			ativo[1]
		)

	print("\nDigite 0 para cancelar.")

	while True:

		entrada = input("\nDigite o ID do ativo: ").strip()

		if entrada == "0":

			print("\nOperação cancelada.")

			conexao.close()

			return

		if not entrada.isdigit():

			print("\nErro: digite apenas números.")

			continue

		ativo_id = int(entrada)

		cursor.execute("""

		SELECT id

		FROM ativos

		WHERE id = ?

		""", (ativo_id,))

		ativo = cursor.fetchone()

		if ativo:
			break

		print("\nID não encontrado.")

	cursor.execute("""

	SELECT
		descricao,
		severidade,
		status

	FROM vulnerabilidades

	WHERE ativo_id = ?

	""", (ativo_id,))

	vulnerabilidades = cursor.fetchall()

	if len(vulnerabilidades) == 0:

		print("\nEste ativo não possui vulnerabilidades registradas.")

	else:

		print("\nVULNERABILIDADES:\n")

		for vuln in vulnerabilidades:

			print("Descrição:", vuln[0])

			print("Severidade:", vuln[1])

			print("Status:", vuln[2])

			print("-" * 30)

	conexao.close()