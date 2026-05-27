from src.dados import ativos
from src.listar import listar_ativos
from src.cadastrar import cadastrar_ativo
from src.editar import editar_ativo

while True:

	print("1.\tPara listar todos os ativos.")
	print("2.\tPara cadastrar novo ativo.")
	print("3.\tAdicionar vulnerabilidades")
	print("4.\tEditar ativo")
	print("10.\tSair.")

	while True:

		try:

			escolha = int(input("Diga o numero que deseja realizar: "))

			if escolha in [1,2,4,10]:
				break

			else:
				print("Erro! Tente novamente.")

		except ValueError:
			print("Digite apenas numeros.")

	if escolha == 1:
		listar_ativos(ativos)

	elif escolha == 2:
		cadastrar_ativo(ativos)

	elif escolha == 4:
		editar_ativo(ativos)

	elif escolha == 10:
		break

	else:
		print("Erro! Tente novamente.")