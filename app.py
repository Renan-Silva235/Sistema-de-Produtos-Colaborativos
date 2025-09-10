from telas.gerenciadorTelas.gerenciador_telas import GerenciadorTelas

def RodarPrograma():
    gerenciador = GerenciadorTelas()
    gerenciador.iniciar("TelaAdministrador")


if __name__ == "__main__":
    RodarPrograma()
