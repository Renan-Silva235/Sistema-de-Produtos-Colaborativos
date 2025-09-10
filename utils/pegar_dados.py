from validacoes.validacoes import Validacoes
import time
from utils.sistema import limpar_tela
def pegar_dados_alimenticios():
    """Essa função pega todos os dados de produtos alimentícios, e retorna um objeto ou uma exceção
    se o tipo de dado for inválido
    """

    while True:
        try:
            produto = input("Digite o nome do produto: ").title()
            peso = input("Digite o peso do produto: ").title()
            validade = input("Digite a validade do produto utilizando '/' para separar dd/mm/yy: ")
            quantidade = int(input("Digite a quantidade total de produtos: "))
            origem = input("Digite a Origem do Produto: ")
        except ValueError:
            print("Tipo de dado inválido")
            continue

        if not Validacoes.validar_formato_data(validade):
            print("Formato de data inválido. Use (dd/mm/yy)")
            continue

        if not Validacoes.validar_peso(peso):
            print("Formato de peso inválido, utilize uma unidade de medida (Kg, G, L ou Ml)")
            continue
        break

    return {
            "nome": produto,
            "peso": peso,
            "validade": validade,
            "quantidade": quantidade,
            "Origem": origem
        }


def pegar_dados_vestuario():
    try:
        tipo_roupa = input("Digite o tipo do vestuário (meia, calça, blusa, etc): ").title()
        marca = input("Marca do Produto: ").title()
        cor = input("Cor do Produto: ").title()
        tamanho = input("Tamanho (M,P,G): ").title()
        quantidade = int(input("Digite a quantidade: "))
        origem = input("Digite a Origem do Produto: ").title()
    except ValueError:
        print("Dado Inválido.")
        time.sleep(1)
        limpar_tela()
        pegar_dados_vestuario()

    return {
        "tipo": tipo_roupa,
        "marca": marca,
        "cor": cor,
        "tamanho": tamanho,
        "quantidade": quantidade,
        "origem": origem
    }


def pegar_dados_domestico():
    try:
        produto = input("Digite o nome do objeto: ").title()
        cor = input("Digite a cor do objeto: ").title()
        quantidade = int(input("Digite a quantidade: "))
        origem = input("Digite a Origem: ").title()
    except ValueError:
        print("Dado Inválido")
        time.sleep(1)
        limpar_tela()
        pegar_dados_domestico()

    return {
        "produto": produto,
        "cor": cor,
        "quantidade": quantidade,
        "origem": origem
    }


