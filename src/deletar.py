from database.connection import conectar

def deletar_ativo():

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

	print("\nATIVOS DISPONÍVEIS:\n")

	for ativo in ativos:

		print(
			"ID:",
			ativo[0],
			"-",
			ativo[1]
		)

	while True:

		try:

			iddeletar = int(input("\nDigite o ID do ativo que deseja deletar: "))

			cursor.execute("""

			SELECT id, nome

			FROM ativos

			WHERE id = ?

			""", (iddeletar,))

			ativo = cursor.fetchone()

			if ativo:
				break

			else:
				print("ID não encontrado.")

		except ValueError:
			print("Digite apenas números.")

	print("\nVocê deseja deletar o ativo:",ativo[1])

	confirmacao = input("Digite S para confirmar: ").strip().lower()

	if confirmacao == "s":

		cursor.execute("""

		DELETE FROM ativos

		WHERE id = ?

		""", (iddeletar,))

		conexao.commit()

		print("\nAtivo deletado com sucesso.")

		print("As vulnerabilidades associadas também foram removidas.")

	else:

		print("\nOperação cancelada.")

	conexao.close()