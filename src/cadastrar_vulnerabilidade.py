from src.modelo import Vulnerabilidade
from src.dados import severidades, status_lista


class CadastrarVulnerabilidade:

	def __init__(self, ativo_repo, vuln_repo):

		self.ativo_repo = ativo_repo
		self.vuln_repo = vuln_repo

	def executar(self):

		ativos = self.ativo_repo.listar_ids_nomes()

		if len(ativos) == 0:

			print("\nNenhum ativo cadastrado.")

			return

		print("\nATIVOS:\n")

		ativos_dict = {}

		for ativo in ativos:

			ativos_dict[ativo[0]] = ativo[1]

			print(
				"ID:",
				ativo[0],
				"-",
				ativo[1]
			)

		print("\nDigite 0 para cancelar.")

		while True:

			entrada = input(
				"\nDigite o ID do ativo: "
			).strip()

			if entrada == "0":

				print("\nOperação cancelada.")

				return

			if not entrada.isdigit():

				print("\nDigite apenas números.")

				continue

			ativo_id = int(entrada)

			if ativo_id in ativos_dict:
				break

			print("\nID inválido.")

		while True:

			descricao = input("Descrição da vulnerabilidade: ").strip()

			if descricao.lower() == "0":

				print("\nOperação cancelada.")

				return

			if descricao != "":
				break

			print("Descrição inválida.")

		while True:

			categoria = input("Categoria/Tipo: ").strip()

			if categoria.lower() == "0":

				print("\nOperação cancelada.")

				return

			if categoria != "":
				break

			print("Categoria inválida.")

		print("\nSeveridades:\n")

		for i, valor in enumerate(severidades, start=1):

			print(i, "-", valor)

		print("0 - Cancelar")

		while True:

			entrada = input("Escolha a severidade: ").strip()

			if entrada == "0":

				print("\nOperação cancelada.")

				return

			if not entrada.isdigit():

				print("\nDigite apenas números.")

				continue

			escolha = int(entrada)

			if escolha in [1,2,3,4]:

				severidade = severidades[
					escolha - 1
				]

				break

			print("Opção inválida.")

		print("\nStatus:\n")

		for i, valor in enumerate(status_lista, start=1):

			print(i, "-", valor)

		print("0 - Cancelar")

		while True:

			entrada = input("Escolha o status: ").strip()

			if entrada == "0":

				print("\nOperação cancelada.")

				return

			if not entrada.isdigit():

				print("\nDigite apenas números.")

				continue

			escolha = int(entrada)

			if escolha in [1,2,3,4]:

				status = status_lista[
					escolha - 1
				]

				break

			print("Opção inválida.")

		while True:

			usuario = input("Seu nome: ").strip()

			if usuario == "0":

				print("\nOperação cancelada.")

				return

			if usuario != "":
				break

			print("Nome inválido.")

		vuln = Vulnerabilidade(
			ativo_id=ativo_id,
			descricao=descricao,
			categoria=categoria,
			severidade=severidade,
			status=status,
			usuario=usuario
		)

		self.vuln_repo.salvar(vuln)

		print("\nVulnerabilidade cadastrada com sucesso.")
