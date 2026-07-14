from src.modelo import Ativo
from src.dados import tipos_ativos


class CadastrarAtivo:

	def __init__(self, repo):

		self.repo = repo

	def executar(self):

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

		ativo = Ativo(nome=nome, tipo=tipo, local=local, ultimo_usuario=usuario)
		self.repo.salvar(ativo)

		print("\nAtivo cadastrado com sucesso.")
