from database.connection import Database
from src.repositorio import AtivoRepositorio, VulnerabilidadeRepositorio
from src.listar import ListarAtivos
from src.cadastrar import CadastrarAtivo
from src.cadastrar_vulnerabilidade import CadastrarVulnerabilidade
from src.editar import EditarAtivo
from src.listar_vulnerabilidades import ListarVulnerabilidades
from src.buscar import BuscarAtivo
from src.deletar import DeletarAtivo


class CLIApp:

	def __init__(self):

		self.db = Database()
		self.ativo_repo = AtivoRepositorio(self.db)
		self.vuln_repo = VulnerabilidadeRepositorio(self.db)

	def run(self):

		while True:

			self._exibir_menu()
			escolha = self._obter_escolha()
			continuar = self._executar_opcao(escolha)

			if not continuar:
				break

	def _exibir_menu(self):

		print("\n" + "=" * 40)
		print("   SISTEMA DE GERENCIAMENTO DE ATIVOS")
		print("=" * 40)
		print("1.\tListar todos os ativos")
		print("2.\tCadastrar novo ativo")
		print("3.\tAdicionar vulnerabilidade")
		print("4.\tEditar ativo")
		print("5.\tListar vulnerabilidades")
		print("6.\tBuscar ativo")
		print("7.\tDeletar ativo")
		print("10.\tSair")
		print("=" * 40)

	def _obter_escolha(self):

		while True:
			try:
				escolha = int(input("Escolha uma opção: "))
				if escolha in [1, 2, 3, 4, 5, 6, 7, 10]:
					return escolha
				else:
					print("Erro! Opção inválida. Tente novamente.")
			except ValueError:
				print("Digite apenas números.")

	def _executar_opcao(self, escolha):

		if escolha == 1:
			op = ListarAtivos(self.ativo_repo)
			op.executar()

		elif escolha == 2:
			op = CadastrarAtivo(self.ativo_repo)
			op.executar()

		elif escolha == 3:
			op = CadastrarVulnerabilidade(self.ativo_repo, self.vuln_repo)
			op.executar()

		elif escolha == 4:
			op = EditarAtivo(self.ativo_repo)
			op.executar()

		elif escolha == 5:
			op = ListarVulnerabilidades(self.ativo_repo, self.vuln_repo)
			op.executar()

		elif escolha == 6:
			op = BuscarAtivo(self.ativo_repo)
			op.executar()

		elif escolha == 7:
			op = DeletarAtivo(self.ativo_repo)
			op.executar()

		elif escolha == 10:
			print("\nSaindo... Até logo!")
			return False

		return True


def main():

	app = CLIApp()
	app.run()


if __name__ == "__main__":
	main()
