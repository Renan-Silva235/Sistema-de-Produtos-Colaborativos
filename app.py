from telas.menus.tela_menu_inicial import TelaInicial


class RodarPrograma:
    """
    Classe responsável por iniciar a execução do programa.

    Contém o método estático run() que inicia a tela inicial do sistema.
    """

    @staticmethod
    def run():
        """
        Inicia a execução do programa, exibindo a tela inicial.

        :return: None
        """
        iniciar = TelaInicial()
        iniciar.mostrar()


if __name__ == "__main__":
    RodarPrograma.run()
