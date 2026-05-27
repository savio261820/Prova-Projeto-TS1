from src.dados import tipos_ativos

def cadastrar_ativo(ativos):

	if len(ativos) == 0:
		idativo = 1
	else:
		idativo = max(ativos) + 1

	print("Cadastrar novo(s) ativo(s).")

	# USUARIO
	while True:

		usuario = input(
			"Qual o seu nome(usuario)?: "
		).strip()

		if usuario != "":
			break

		else:
			print(
				"Nome de usuario invalido."
			)

	# NOME
	while True:

		nome = input(
			"Diga o nome do ativo: "
		).strip()

		if nome != "":
			break

		else:
			print("Nome invalido.")

	# TIPO
	while True:

		print("\nTipos de ativos:")

		for idtipo, nometipo in tipos_ativos.items():
			print(idtipo, "-", nometipo)

		tipo_input = input(
			"Digite o ID ou o nome do tipo: "
		).strip().lower()

		# POR ID
		if tipo_input.isdigit():

			tipo_id = int(tipo_input)

			if tipo_id in tipos_ativos:
				tipo = tipos_ativos[tipo_id]
				break

		# POR NOME
		else:

			for valor in tipos_ativos.values():

				if tipo_input == valor.lower():
					tipo = valor
					break

			else:
				print("Tipo invalido.")
				continue

			break

		print("Tipo invalido.")

	# LOCAL
	while True:

		local = input(
			"Diga o local do ativo: "
		).strip()

		if local != "":
			break

		else:
			print("Local invalido.")

	# SALVAR
	ativos[idativo] = {
		"nome": nome,
		"tipo": tipo,
		"local": local,
		"ultimousuario": usuario
	}

	print("Ativo cadastrado com id", idativo)