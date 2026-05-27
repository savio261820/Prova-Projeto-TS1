ativos = {}

tipos_ativos = {
	1: "Servidores",
	2: "Workstations",
	3: "Aparelhos",
	4: "Impressoras"
}

while True:
	print("1.\tPara listar todos os ativos.")
	print("2.\tPara cadastrar novo ativo.")
	print("3.\tAdicionar vulnerabilidades.")
	print("4.\tEditar ativo")

	print("10.\tSair.")


	while True:
		try:
			escolha = int(input("Diga o número que deseja realizar: "))

			if escolha in [1,2,3,4,10]:
				break
			else:
				print("Erro! Tente novamente.")

		except ValueError:
			print("Digite apenas números.")


	#if escolha == int and escolha > 0:
	#	print("ok")
	#else:
	#	print("erro. tente novamente.")

	if escolha == 1:
		print("\n" * 3)
		print("Ativos cadastrados.")

		for idativo, infos in ativos.items():

			print("\n" * 2)
			print("ID:", idativo)
			print("Nome:", infos['nome'])
			print("Tipo:", infos['tipo'])
			print("Local:", infos['local'])
			print("Ultimo usuario:", infos['ultimousuario'])
			print("\n" * 2)

	elif escolha == 2:

		if len(ativos) == 0:
			idativo = 1
		else:
			idativo = max(ativos) + 1

		print("Cadastrar novo(s) ativo(s).")

		while True:
			usuario = input("Qual o seu nome(usuario)?: ").strip()

			if usuario !="":
				break
			else:
				print("Nome de usuario invalido. Erro! Tente novamente.")

		while True:
			nome = input("Diga o nome do ativo: ").strip()
			if nome !="":
				break
			else:
				print("Nome invalido. Erro! Tente novamente.")
#>
		while True:
			print("\nTipos de ativos:")

			for idtipo, nometipo in tipos_ativos.items():
				print(idtipo, "-", nometipo)

			tipo_input = input("Digite o ID ou o nome do tipo: ").strip().lower()

			if tipo_input.isdigit():
				tipo_id = int(tipo_input)

				if tipo_id in tipos_ativos:
					tipo = tipos_ativos[tipo_id]
					break

			else:
				for valor in tipos_ativos.values():
					if tipos_ativos == valor.lower():
						tipos = valor
						break
				else:
					print("Tipo invalido. Erro! Tente novamente.")
					continue
				break
			print("Tipo invalido. Erro! Tente novamente")

#<

		while True:
			local = input("Diga o local do ativo: ")
			if local !="":
				break
			else:
				print("local invalido. Erro! Tente novamente")

		ativos[idativo] = {
			"nome": nome,
			"tipo": tipo,
			"local": local,
			"ultimousuario": usuario
		}

		print("Ativo cadastrado com id", idativo)

	elif escolha == 10:
		break

	elif escolha == 4:

		if len(ativos) == 0:
			print("Nenhum ativo encontrado")

		else:

			print("\nAtivos disponíveis:\n")

			for idativo, infos in ativos.items():
				print("ID:", idativo, "-", infos['nome'])

			while True:

				try:

					ideditar = int(
						input("Digite o ID do ativo que deseja editar: ")
					)

					if ideditar in ativos:
						break
					else:
						print("ID não encontrado.")

				except ValueError:
					print("Digite apenas numeros.")

			ativo = ativos[ideditar]

			print("\nEditando ativo:", ativo['nome'])

			novo_nome = input(
				"Novo nome (ENTER para manter): "
			).strip()

			if novo_nome != "":
				ativo['nome'] = novo_nome

			print("\nTipos disponíveis:\n")

			for idtipo, nometipo in tipos_ativos.items():
				print(idtipo, "-", nometipo)

			novo_tipo = input(
				"Novo tipo (ENTER para manter): "
			).strip().lower()

			if novo_tipo != "":

				if novo_tipo.isdigit():

					tipo_id = int(novo_tipo)

					if tipo_id in tipos_ativos:
						ativo['tipo'] = tipos_ativos[tipo_id]

				else:

					for valor in tipos_ativos.values():

						if novo_tipo == valor.lower():
							ativo['tipo'] = valor
							break

			novo_local = input("Novo local (ENTER para manter): ").strip()

			if novo_local != "":
				ativo['local'] = novo_local

			while True:

				usuario = input("Quem realizou esta alteração?: ").strip()

				if usuario != "":
					break

				print("Nome inválido.")

			ativo['ultimousuario'] = usuario

			print("\nAtivo atualizado com sucesso.")



	else:
		print("Erro! Tente novamente. ")



