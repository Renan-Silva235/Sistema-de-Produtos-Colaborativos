import os


def limpar_tela():
    # Verifica o sistema operacional e executa o comando apropriado
    if os.name == 'nt':  # nt é usado para Windows
        os.system('cls')
    else:  # Assume sistemas POSIX (Linux, macOS)
        os.system('clear')
