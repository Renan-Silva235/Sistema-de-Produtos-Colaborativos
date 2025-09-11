import os

def limpar_tela():
    """Verifica qual tipo de sistema operacional o programa está rodando,
    se for windows a função vai limpar o terminal utilizando o comando 'cls', caso
    seja linux ou MAC a função vai rodar o comando 'clear' para limpar o terminal"""

    # Verifica o sistema operacional e executa o comando apropriado
    if os.name == 'nt':  # nt é usado para Windows
        os.system('cls')
    else:  # Assume sistemas POSIX (Linux, macOS)
        os.system('clear')
