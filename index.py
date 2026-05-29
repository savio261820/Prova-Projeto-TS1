import sys

print("CRUD\tTRABALHO")
print("\nComo deseja executar o código?\n1. Interface gráfica\t(Tkinter)\n2. Terminal\t(CLI)\n0. Sair\t(Exit)")

while True:
    try:
        escolha = int(input("Escolha uma opção: "))
        if escolha in [0, 1, 2]:
            break
        print("Erro! Opção inválida. Tente novamente.")
    except ValueError:
        print("Erro! Digite apenas números.")

if escolha == 0:
    print("\nSaindo... Até logo!\n")
    sys.exit(0)

elif escolha == 1:
    print("\nIniciando interface gráfica...\n")
    try:
        from interface import main as run_gui
        run_gui()
    except ImportError as e:
        print("Erro! Houve esse problema ao rodar interface", e)
        sys.exit(1)

elif escolha == 2:
    print("\nIniciando modo terminal...\n")
    from cli import main as run_cli
    run_cli()