class ListarAtivos:

	def __init__(self, repo):

		self.repo = repo

	def executar(self):

		ativos = self.repo.listar_todos()

		if len(ativos) == 0:

			print("Nenhum ativo cadastrado.")

		else:

			print("\nATIVOS:\n")

			for ativo in ativos:

				print("ID:", ativo.id)
				print("Nome:", ativo.nome)
				print("Tipo:", ativo.tipo)
				print("Local:", ativo.local)
				print("Último usuário:", ativo.ultimo_usuario)

				print("-" * 30)
