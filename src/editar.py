from database.connection import conectar
from src.dados import tipos_ativos

def editar_ativo():

	conexao = conectar()

	cursor = conexao.cursor()

	cursor.execute("""

	SELECT
		id,
		nome

	FROM ativos

	""")

	ativos = cursor.fetchall()

	if len(ativos) == 0:

		print("Nenhum ativo encontrado.")

		conexao.close()

		return

	print("\nAtivos disponíveis:\n")

	for ativo in ativos:
		print("ID:", ativo[0], "-", ativo[1])

	while True:

		try:

			ideditar = int(
				input(
					"Digite o ID do ativo que deseja editar: "
				)
			)

			cursor.execute("""

			SELECT
				id,
				nome,
				tipo,
				local,
				ultimo_usuario

			FROM ativos

			WHERE id = ?

			""", (ideditar,))

			ativo = cursor.fetchone()

			if ativo:
				break

			else:
				print("ID não encontrado.")

		except ValueError:
			print("Digite apenas números.")

	print("\nEditando ativo:", ativo[1])

	novo_nome = input("Novo nome (ENTER para manter): ").strip()

	if novo_nome == "":
		novo_nome = ativo[1]

	print("\nTipos disponíveis:\n")

	for idtipo, nometipo in tipos_ativos.items():
		print(idtipo, "-", nometipo)

	novo_tipo = input("Novo tipo (ENTER para manter): ").strip().lower()

	if novo_tipo == "":

		novo_tipo = ativo[2]

	else:

		if novo_tipo.isdigit():

			tipo_id = int(novo_tipo)

			if tipo_id in tipos_ativos:
				novo_tipo = tipos_ativos[tipo_id]

			else:
				novo_tipo = ativo[2]

		else:

			encontrado = False

			for valor in tipos_ativos.values():

				if novo_tipo == valor.lower():
					novo_tipo = valor
					encontrado = True
					break

			if encontrado == False:
				novo_tipo = ativo[2]

	novo_local = input(
		"Novo local (ENTER para manter): "
	).strip()

	if novo_local == "":
		novo_local = ativo[3]

	while True:

		usuario = input("Quem realizou esta alteração?: ").strip()

		if usuario != "":
			break

		print("Nome inválido.")

	cursor.execute("""

	UPDATE ativos

	SET
		nome = ?,
		tipo = ?,
		local = ?,
		ultimo_usuario = ?

	WHERE id = ?

	""", (
		novo_nome,
		novo_tipo,
		novo_local,
		usuario,
		ideditar
	))

	conexao.commit()

	print("\nAtivo atualizado com sucesso.")

	conexao.close()