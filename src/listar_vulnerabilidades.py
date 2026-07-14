class ListarVulnerabilidades:

	def __init__(self, ativo_repo, vuln_repo):

		self.ativo_repo = ativo_repo
		self.vuln_repo = vuln_repo

	def executar(self):

		ativos = self.ativo_repo.listar_ids_nomes()

		if len(ativos) == 0:

			print("\nNenhum ativo cadastrado.")

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

				return

			if not entrada.isdigit():

				print("\nErro: digite apenas números.")

				continue

			ativo_id = int(entrada)

			ativo = self.ativo_repo.buscar_por_id(ativo_id)

			if ativo:
				break

			print("\nID não encontrado.")

		vulnerabilidades = self.vuln_repo.listar_por_ativo_id(ativo_id)

		if len(vulnerabilidades) == 0:

			print("\nEste ativo não possui vulnerabilidades registradas.")

		else:

			print("\nVULNERABILIDADES:\n")

			for vuln in vulnerabilidades:

				print("Descrição:", vuln[0])

				print("Severidade:", vuln[1])

				print("Status:", vuln[2])

				print("-" * 30)
