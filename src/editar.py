from src.dados import tipos_ativos

def editar_ativo(ativos):

	if len(ativos) == 0:
		print("Nenhum ativo encontrado")

	else:

		print("\nAtivos disponíveis:\n")

		for idativo, infos in ativos.items():
			print("ID:", idativo, "-", infos['nome'])

		# ESCOLHER ID
		while True:

			try:

				ideditar = int(input("Digite o ID do ativo que deseja editar: "))

				if ideditar in ativos:
					break

				else:
					print("ID não encontrado.")

			except ValueError:
				print("Digite apenas numeros.")

		ativo = ativos[ideditar]

		print("\nEditando ativo:", ativo['nome'])

		# NOVO NOME
		novo_nome = input("Novo nome (ENTER para manter): ").strip()

		if novo_nome != "":
			ativo['nome'] = novo_nome

		# NOVO TIPO
		print("\nTipos disponíveis:\n")

		for idtipo, nometipo in tipos_ativos.items():
			print(idtipo, "-", nometipo)

		novo_tipo = input("Novo tipo (ENTER para manter): ").strip().lower()

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

		# NOVO LOCAL
		novo_local = input("Novo local (ENTER para manter): ").strip()

		if novo_local != "":
			ativo['local'] = novo_local

		# USUARIO
		while True:

			usuario = input("Quem realizou esta alteração?: ").strip()

			if usuario != "":
				break

			print("Nome inválido.")

		ativo['ultimousuario'] = usuario

		print("\nAtivo atualizado com sucesso.")