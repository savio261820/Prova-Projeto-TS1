class BuscarAtivo:

	def __init__(self, repo):

		self.repo = repo

	def executar(self):

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

			ids = self.repo.listar_ids_disponiveis()

			print("\nIDs disponíveis:\n")

			for valor in ids:
				print(valor)

			while True:

				try:
					id_busca = int(input("\nDigite o ID: "))
					break

				except ValueError:
					print("Digite apenas números.")

			resultados = self.repo.buscar_por_id(id_busca)

			if resultados:
				resultados = [resultados]
			else:
				resultados = []

		elif escolha == 2:

			nomes = self.repo.listar_nomes_disponiveis()

			print("\nNomes disponíveis:\n")

			for valor in nomes:
				print(valor)

			nome_busca = input("\nDigite o nome: ").strip()

			resultados = self.repo.buscar_por_nome(nome_busca)

		elif escolha == 3:

			usuarios = self.repo.listar_usuarios_disponiveis()

			print("\nUsuários disponíveis:\n")

			for valor in usuarios:
				print(valor)

			usuario_busca = input("\nDigite o usuário: ").strip()

			resultados = self.repo.buscar_por_usuario(usuario_busca)

		elif escolha == 4:

			locais = self.repo.listar_locais_disponiveis()

			print("\nLocais disponíveis:\n")

			for valor in locais:
				print(valor)

			local_busca = input("\nDigite o local: ").strip()

			resultados = self.repo.buscar_por_local(local_busca)

		if len(resultados) == 0:

			print("\nNenhum ativo encontrado.")

		else:

			print("\nRESULTADOS:\n")

			for ativo in resultados:

				print("ID:", ativo.id)
				print("Nome:", ativo.nome)
				print("Tipo:", ativo.tipo)
				print("Local:", ativo.local)
				print("Último usuário:", ativo.ultimo_usuario)

				print("-" * 30)
