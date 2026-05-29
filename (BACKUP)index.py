from src.listar import listar_ativos
from src.cadastrar import cadastrar_ativo
from src.editar import editar_ativo
from src.cadastrar_vulnerabilidade import cadastrar_vulnerabilidade
from src.listar_vulnerabilidades import listar_vulnerabilidades
from src.deletar import deletar_ativo
from src.buscar import buscar_ativos
import database.schema

while True:

	print("1.\tPara listar todos os ativos.")
	print("2.\tPara cadastrar novo ativo.")
	print("3.\tAdicionar vulnerabilidades")
	print("4.\tEditar ativo")
	print("5.\tListar vulnerabilidades")
	print("6.\tBuscar ativo.")
	print("7.\tDeletar ativo.")
	print("10.\tSair.")

	while True:

		try:

			escolha = int(input("Diga o numero que deseja realizar: "))

			if escolha in [1,2,3,4,10,5,6,7]:
				break

			else:
				print("Erro! Tente novamente.")

		except ValueError:
			print("Digite apenas numeros.")

	if escolha == 1:
		listar_ativos()

	elif escolha == 2:
		cadastrar_ativo()

	elif escolha == 3:
		cadastrar_vulnerabilidade()

	elif escolha == 5:
		listar_vulnerabilidades()

	elif escolha == 4:
		editar_ativo()

	elif escolha == 6:
		buscar_ativos()
	elif escolha == 7:
		deletar_ativo()





	elif escolha == 10:
		break

	else:
		print("Erro! Tente novamente.")