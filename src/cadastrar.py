from database.connection import conectar

tipos_ativos = {
	1: "Servidores",
	2: "Workstations",
	3: "Aparelhos",
	4: "Impressoras"
}

def cadastrar_ativo():

	conexao = conectar()

	cursor = conexao.cursor()

	print("Cadastrar novo ativo.")

	while True:

		usuario = input("Qual o seu nome(usuario)?: ").strip()

		if usuario != "":
			break

		print("Nome inválido. Erro! Tente novamente.")

	while True:

		nome = input("Diga o nome do ativo: ").strip()

		if nome != "":
			break

		print("Nome inválido. Erro! Tente novamente.")

	while True:

		print("\nTipos disponíveis:\n")

		for idtipo, nometipo in tipos_ativos.items():
			print(idtipo, "-", nometipo)

		tipo_input = input("Digite o ID ou nome: ").strip().lower()

		if tipo_input.isdigit():

			tipo_id = int(tipo_input)

			if tipo_id in tipos_ativos:
				tipo = tipos_ativos[tipo_id]
				break

		else:

			for valor in tipos_ativos.values():

				if tipo_input == valor.lower():
					tipo = valor
					break

			else:
				print("Tipo inválido.")
				continue

			break

		print("Tipo inválido.")

	while True:

		local = input("Diga o local do ativo: ").strip()

		if local != "":
			break

		print("Local inválido.")

	cursor.execute("""

	INSERT INTO ativos (
		nome,
		tipo,
		local,
		ultimo_usuario
	)

	VALUES (?, ?, ?, ?)

	""", (
		nome,
		tipo,
		local,
		usuario
	))

	conexao.commit()

	print("\nAtivo cadastrado com sucesso.")

	conexao.close()