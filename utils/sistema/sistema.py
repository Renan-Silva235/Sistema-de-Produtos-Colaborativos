import os
from datetime import datetime
from locale import setlocale, LC_ALL


def limpar_tela():
    """Verifica qual tipo de sistema operacional o programa está rodando,
    se for windows a função vai limpar o terminal utilizando o comando 'cls', caso
    seja linux ou MAC a função vai rodar o comando 'clear' para limpar o terminal"""

    # Verifica o sistema operacional e executa o comando apropriado
    if os.name == 'nt':  # nt é usado para Windows
        os.system('cls')
    else:  # Assume sistemas POSIX (Linux, macOS)
        os.system('clear')


def data_hora_atual():
    """
    Retorna a data e hora atual no formato '%d/%m/%Y %H:%M:%S'.

    Exemplo:
        28/06/2022 15:30:00
    """
    setlocale(LC_ALL, 'pt_BR.utf-8')
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')
