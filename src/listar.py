def listar_ativos(ativos):

	print("\n" * 3)
	print("Ativos cadastrados.")

	if len(ativos) == 0:
		print("Nenhum ativo cadastrado.")

	else:

		for idativo, infos in ativos.items():

			print("\n" * 2)
			print("ID:", idativo)
			print("Nome:", infos['nome'])
			print("Tipo:", infos['tipo'])
			print("Local:", infos['local'])
			print("Ultimo usuario:", infos['ultimousuario'])
			print("\n" * 2)