import sqlite3

def conectar():

	conexao = sqlite3.connect("database/security.db")

	return conexao