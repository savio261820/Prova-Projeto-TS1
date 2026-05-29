from database.connection import conectar

def listar_ativos():

	conexao = conectar()

	cursor = conexao.cursor()

	cursor.execute("""

	SELECT
		id,
		nome,
		tipo,
		local,
		ultimo_usuario

	FROM ativos

	""")

	ativos = cursor.fetchall()

	if len(ativos) == 0:

		print("Nenhum ativo cadastrado.")

	else:

		print("\nATIVOS:\n")

		for ativo in ativos:

			print("ID:", ativo[0])
			print("Nome:", ativo[1])
			print("Tipo:", ativo[2])
			print("Local:", ativo[3])
			print("Último usuário:", ativo[4])

			print("-" * 30)

	conexao.close()