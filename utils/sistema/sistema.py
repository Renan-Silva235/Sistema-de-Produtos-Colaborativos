import os
from datetime import datetime
from locale import setlocale, LC_ALL


class Sistema:
    """
    Classe responsável por funções utilitárias do sistema.

    Fornece métodos estáticos para limpar a tela do terminal e obter
    data e hora atual formatadas.
    """
    @staticmethod
    def limpar_tela():
        """
        Limpa a tela do terminal de acordo com o sistema operacional.

        Utiliza o comando 'cls' no Windows e 'clear' em sistemas Linux/Mac.

        :return: None
        """

        # Verifica o sistema operacional e executa o comando apropriado
        if os.name == 'nt':  # nt é usado para Windows
            os.system('cls')
        else:  # Assume sistemas POSIX (Linux, macOS)
            os.system('clear')


    @staticmethod
    def data_hora_atual():
        """
        Retorna a data e hora atual formatada em português brasileiro.

        Formato retornado: dd/mm/aaaa HH:MM:SS

        :return: String com a data e hora atual no formato 'dd/mm/aaaa HH:MM:SS'

        Exemplo:
            "28/06/2022 15:30:00"
        """
        setlocale(LC_ALL, 'pt_BR.utf-8')
        return datetime.now().strftime('%d/%m/%Y %H:%M:%S')
