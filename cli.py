from src.listar import listar_ativos
from src.cadastrar import cadastrar_ativo
from src.editar import editar_ativo
from src.cadastrar_vulnerabilidade import cadastrar_vulnerabilidade
from src.listar_vulnerabilidades import listar_vulnerabilidades
from src.deletar import deletar_ativo
from src.buscar import buscar_ativos
import database.schema


def main():
	while True:

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

		while True:
			try:
				escolha = int(input("Escolha uma opção: "))
				if escolha in [1, 2, 3, 4, 5, 6, 7, 10]:
					break
				else:
					print("Erro! Opção inválida. Tente novamente.")
			except ValueError:
				print("Digite apenas números.")

		if escolha == 1:
			listar_ativos()

		elif escolha == 2:
			cadastrar_ativo()

		elif escolha == 3:
			cadastrar_vulnerabilidade()

		elif escolha == 4:
			editar_ativo()

		elif escolha == 5:
			listar_vulnerabilidades()

		elif escolha == 6:
			buscar_ativos()

		elif escolha == 7:
			deletar_ativo()

		elif escolha == 10:
			print("\nSaindo... Até logo!")
			break

		else:
			print("Erro! Tente novamente.")


if __name__ == "__main__":
	main()
