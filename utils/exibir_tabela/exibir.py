from tabulate import tabulate

class CriarTabelas:

    @staticmethod
    def exibir_tabela(dados, titulo=""):
        """
        Exibe uma tabela com base nos dados informados.

        :param dados: Pode ser um dicionário, uma lista de dicionários ou uma lista simples.
        :param titulo: O título da tabela, default é vazio.
        """
        print(f"\n{titulo}\n")

        if isinstance(dados, dict):
            # Caso seja apenas 1 registro (dict)
            tabela = [[k, v] for k, v in dados.items()]
            print(tabulate(tabela, headers=["Dados", "Informações"], tablefmt="fancy_grid"))

        elif isinstance(dados, list) and len(dados) > 0:
            if isinstance(dados[0], dict):
                # Caso seja lista de dicionários
                cabecalhos = dados[0].keys()
                tabela = [list(item.values()) for item in dados]
                print(tabulate(tabela, headers=cabecalhos, tablefmt="fancy_grid"))
            else:
                # Caso seja lista simples
                print(tabulate([[item] for item in dados], headers=["informações"], tablefmt="fancy_grid"))

        else:
            print("Nenhum dado para exibir.")
