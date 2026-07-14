class DeletarAtivo:

	def __init__(self, repo):

		self.repo = repo

	def executar(self):

		ativos = self.repo.listar_ids_nomes()

		if len(ativos) == 0:

			print("\nNenhum ativo cadastrado.")

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

				ativo = self.repo.buscar_por_id(iddeletar)

				if ativo:
					break

				else:
					print("ID não encontrado.")

			except ValueError:
				print("Digite apenas números.")

		print("\nVocê deseja deletar o ativo:", ativo.nome)

		confirmacao = input("Digite S para confirmar: ").strip().lower()

		if confirmacao == "s":

			self.repo.deletar(iddeletar)

			print("\nAtivo deletado com sucesso.")

			print("As vulnerabilidades associadas também foram removidas.")

		else:

			print("\nOperação cancelada.")
