from tabulate import tabulate

def exibir_tabela(dados, titulo=""):
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
