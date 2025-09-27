from validacoes.validacoes_produtos import Validacoes
import time
from utils.sistema.sistema import limpar_tela
def pegar_dados_alimenticios():
    """Essa função pega todos os dados de produtos alimentícios que o usuário, e retorna um objeto ou uma exceção
    se o tipo de dado for inválido
    """

    try:
        produto = input("Digite o nome do produto: ").title()
        peso = input("Digite o peso do produto (Acrescente a unidade de medida: Kg, G, L, Ml): ").title()
        validade = input("Digite a validade do produto utilizando '/' para separar dd/mm/yy: ")
        quantidade = int(input("Digite a quantidade total de produtos: "))
    except ValueError:
        print("Tipo de dado inválido")
        time.sleep(2)
        limpar_tela()
        return

    if not Validacoes.validar_formato_data(validade):
        print("Formato de data inválido. Use (dd/mm/yy)")
        time.sleep(2)
        limpar_tela()
        return

    if not Validacoes.validar_peso(peso):
        print("Formato de peso inválido, utilize uma unidade de medida (Kg, G, L ou Ml)")
        time.sleep(2)
        limpar_tela()
        return

    if not Validacoes.validar_campos(produto):
        print("Nenhum campo pode estar vazio")
        time.sleep(2)
        limpar_tela()
        return

    return {
        "nome": produto,
        "peso": peso,
        "validade": validade,
        "quantidade": quantidade,
        "id_doadores": []
    }


def pegar_dados_vestuario():
    """Essa função pega todos os dados de vestimentas que o usuário, e retorna um objeto ou uma exceção
    se o tipo de dado for inválido
    """

    try:
        tipo_roupa = input("Digite o tipo da roupa (meia, calça, blusa, etc): ").title()
        marca = input("Marca do Produto: ").title()
        cor = input("Cor do Produto: ").title()
        tamanho = input("Defina os seguintes tamanhos: \n"
                        "- utilize números para o tamanho dos Calçados \n" \
                        "- Utilize os as medidas (P, M, G, GG) para roupas:\n" \
                        "TAMANHO: ").upper()
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Dado Inválido.")
        time.sleep(2)
        limpar_tela()
        return

    if not Validacoes.validar_campos(tipo_roupa, marca, cor):
        print("Nenhum campo pode estar vazio")
        time.sleep(2)
        limpar_tela()
        return

    if not Validacoes.validar_tamanho_vestuario(tamanho):
        print("Tipo de tamanho inválido")
        time.sleep(2)
        limpar_tela()
        return

    return {
        "tipo": tipo_roupa,
        "marca": marca,
        "cor": cor,
        "tamanho": tamanho,
        "quantidade": quantidade,
        "id_doadores": []
    }


def pegar_dados_domestico():
    """Essa função pega todos os dados de produtos domésticos que o usuário digitar, e retorna um objeto ou uma exceção
    se o tipo de dado for inválido
    """

    try:
        produto = input("Digite o nome do objeto: ").title()
        cor = input("Digite a cor do objeto: ").title()
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Dado Inválido")
        time.sleep(2)
        limpar_tela()
        return False

    if not Validacoes.validar_campos(produto, cor):
        print("Nenhum campo pode estar vazio")
        time.sleep(2)
        limpar_tela()
        return
    return {
        "produto": produto,
        "cor": cor,
        "quantidade": quantidade,
        "id_doadores": []
    }


