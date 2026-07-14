from src.dados import tipos_ativos


class EditarAtivo:

	def __init__(self, repo):

		self.repo = repo

	def executar(self):

		ativos = self.repo.listar_ids_nomes()

		if len(ativos) == 0:

			print("Nenhum ativo encontrado.")

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

				ativo = self.repo.buscar_por_id(ideditar)

				if ativo:
					break

				else:
					print("ID não encontrado.")

			except ValueError:
				print("Digite apenas números.")

		print("\nEditando ativo:", ativo.nome)

		novo_nome = input("Novo nome (ENTER para manter): ").strip()

		if novo_nome == "":
			novo_nome = ativo.nome

		print("\nTipos disponíveis:\n")

		for idtipo, nometipo in tipos_ativos.items():
			print(idtipo, "-", nometipo)

		novo_tipo = input("Novo tipo (ENTER para manter): ").strip().lower()

		if novo_tipo == "":

			novo_tipo = ativo.tipo

		else:

			if novo_tipo.isdigit():

				tipo_id = int(novo_tipo)

				if tipo_id in tipos_ativos:
					novo_tipo = tipos_ativos[tipo_id]

				else:
					novo_tipo = ativo.tipo

			else:

				encontrado = False

				for valor in tipos_ativos.values():

					if novo_tipo == valor.lower():
						novo_tipo = valor
						encontrado = True
						break

				if encontrado == False:
					novo_tipo = ativo.tipo

		novo_local = input(
			"Novo local (ENTER para manter): "
		).strip()

		if novo_local == "":
			novo_local = ativo.local

		while True:

			usuario = input("Quem realizou esta alteração?: ").strip()

			if usuario != "":
				break

			print("Nome inválido.")

		ativo.nome = novo_nome
		ativo.tipo = novo_tipo
		ativo.local = novo_local
		ativo.ultimo_usuario = usuario

		self.repo.atualizar(ativo)

		print("\nAtivo atualizado com sucesso.")
