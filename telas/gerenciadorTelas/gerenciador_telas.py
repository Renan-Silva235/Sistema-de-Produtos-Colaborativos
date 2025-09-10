from telas.tela_inicial import TelaInicial
from telas.tela_login import TelaLogin
from telas.tela_administrador import TelaAdministrador
from telas.tela_menu_cadastros import TelaMenuCadastro
from telas.tela_recuperar_senha import TelaRecuperarSenha
from telas.tela_cadastro_produtos import TelaCadastrarProdutos

class GerenciadorTelas:
    """Essa classe gerencia o fluxo de telas, evitando erro de import circular"""

    def iniciar(self, nome_tela):
        self.mudar_tela(nome_tela)

    def mudar_tela(self, nome_tela):
        mapa_telas = {
            "TelaInicial": TelaInicial,
            "TelaLogin": TelaLogin,
            "TelaAdministrador": TelaAdministrador,
            "TelaMenuCadastro": TelaMenuCadastro,
            "TelaRecuperarSenha": TelaRecuperarSenha,
            "TelaCadastrarProdutos": TelaCadastrarProdutos
        }

        classe_tela = mapa_telas.get(nome_tela)

        if not classe_tela:
            raise ValueError(f"Tela '{nome_tela}' não existe no gerenciador.")

        self.tela_atual = classe_tela(self)
        self.tela_atual.mostrar()
