from database.connection import conectar

def buscar_ativos():

	conexao = conectar()

	cursor = conexao.cursor()

	print("\nBUSCAR ATIVOS\n")

	print("1.\tBuscar por ID")
	print("2.\tBuscar por nome")
	print("3.\tBuscar por usuário")
	print("4.\tBuscar por local")

	while True:

		try:
			escolha = int(input("Escolha uma opção: "))
			if escolha in [1,2,3,4]:
				break

			print("Opção inválida.")

		except ValueError:
			print("Digite apenas números.")

	if escolha == 1:

		cursor.execute("""

		SELECT DISTINCT id

		FROM ativos

		""")

		ids = cursor.fetchall()

		print("\nIDs disponíveis:\n")

		for valor in ids:
			print(valor[0])

		while True:

			try:
				id_busca = int(input("\nDigite o ID: "))
				break

			except ValueError:
				print("Digite apenas números.")

		cursor.execute("""

		SELECT
			id,
			nome,
			tipo,
			local,
			ultimo_usuario

		FROM ativos

		WHERE id = ?

		""", (id_busca,))

		resultados = cursor.fetchall()

	elif escolha == 2:

		cursor.execute("""

		SELECT DISTINCT nome

		FROM ativos

		ORDER BY nome

		""")

		nomes = cursor.fetchall()

		print("\nNomes disponíveis:\n")

		for valor in nomes:
			print(valor[0])

		nome_busca = input("\nDigite o nome: ").strip()

		cursor.execute("""

		SELECT
			id,
			nome,
			tipo,
			local,
			ultimo_usuario

		FROM ativos

		WHERE LOWER(nome) = LOWER(?)

		""", (nome_busca,))

		resultados = cursor.fetchall()

	elif escolha == 3:

		cursor.execute("""

		SELECT DISTINCT ultimo_usuario

		FROM ativos

		ORDER BY ultimo_usuario

		""")

		usuarios = cursor.fetchall()

		print("\nUsuários disponíveis:\n")

		for valor in usuarios:
			print(valor[0])

		usuario_busca = input("\nDigite o usuário: ").strip()

		cursor.execute("""

		SELECT
			id,
			nome,
			tipo,
			local,
			ultimo_usuario

		FROM ativos

		WHERE LOWER(ultimo_usuario) = LOWER(?)

		""", (usuario_busca,))

		resultados = cursor.fetchall()

	elif escolha == 4:

		cursor.execute("""

		SELECT DISTINCT local

		FROM ativos

		ORDER BY local

		""")

		locais = cursor.fetchall()

		print("\nLocais disponíveis:\n")

		for valor in locais:
			print(valor[0])

		local_busca = input("\nDigite o local: ").strip()

		cursor.execute("""

		SELECT
			id,
			nome,
			tipo,
			local,
			ultimo_usuario

		FROM ativos

		WHERE LOWER(local) = LOWER(?)

		""", (local_busca,))

		resultados = cursor.fetchall()

	if len(resultados) == 0:

		print("\nNenhum ativo encontrado.")

	else:

		print("\nRESULTADOS:\n")

		for ativo in resultados:

			print("ID:", ativo[0])
			print("Nome:", ativo[1])
			print("Tipo:", ativo[2])
			print("Local:", ativo[3])
			print("Último usuário:", ativo[4])

			print("-" * 30)

	conexao.close()