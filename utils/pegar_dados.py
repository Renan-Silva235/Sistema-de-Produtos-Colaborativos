from validacoes.validacoes import Validacoes

def pegar_dados_alimenticios():
    """Essa função pega todos os dados de produtos alimentícios, e retorna um objeto ou uma exceção
    se o tipo de dado for inválido
    """

    while True:
        try:
            produto = input("Digite o nome do produto: ").title()
            peso = int(input("Digite o peso do produto: "))
            validade = input("Digite a validade do produto utilizando '/' para separar dd/mm/yy: ")
            quantidade = int(input("Digite a quantidade total de produtos: "))
            origem = input("Digite a Origem do Produto: ")
        except ValueError:
            print("Tipo de dado inválido")
            continue

        if not Validacoes.validar_formato_data(validade):
            print(f"Formato de data inválido. Use (dd/mm/yy)")
            continue
        break

    return {
            "nome": produto,
            "peso": peso,
            "validade": validade,
            "quantidade": quantidade,
            "Origem": origem
        }
