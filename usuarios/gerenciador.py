import os
import json
import ctypes
import sys
from tabulate import tabulate

class Gerenciador:
    def __init__(self, arquivo):
        """O construtor recebe o arquivo json que será manipulado"""
        self.arquivo = arquivo


    def login(self, email, senha):
        """Esse método recebe email e senha para fazer login no sistema"""
        dados = self.listar()
        for dado in dados:
            if dado["email"] == email and dado["senha"] == senha:
                return dado

        return False


    def listar(self):
        """Esse método lista todos os objetos que estão salvos no json"""
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                conteudo = arq.read().strip()
                if not conteudo:
                    return []  # arquivo vazio
                return json.loads(conteudo)

        return []


    def cadastrar(self, dados):

        """Esse método configura a função salvarNoJson que foi escrita em C, para ser reutilizada no
            python, na função salvarNoJson abaixo, foi configurada os tipos de argumentos que a função recebe
            (argstype) e o tipo de retorno que ela fornece (restype)."""

        if sys.platform.startswith("win"):
            libname = "salvarJson.dll"
        elif sys.platform.startswith("linux"):
            libname = "salvarJson.so"
        else:
            raise OSError("Sistema operacional não suportado")

        lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build", libname))
        lib = ctypes.CDLL(lib_path)
        lib.salvarNoJson.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        lib.salvarNoJson.restype = None

        json_str = json.dumps(dados.objeto())
        lib.salvarNoJson(self.arquivo.encode("utf-8"), json_str.encode("utf-8"))



    def atualizar(self, chave, valor_atual, novo_valor):
        dados = self.listar()
        for dado in dados:
            if dado[chave] == valor_atual:
                dado[chave] = novo_valor

        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def consulta(self, dado):
        lista = self.listar()
        resultados = []

        for item in lista:
            if any(str(dado).lower() in str(valor).lower() for valor in item.values()):
                resultados.append(item)

        if not resultados:
            return "Nenhum resultado encontrado."

        # pegar cabeçalhos das chaves do dicionário
        cabecalhos = resultados[0].keys()

        # transformar lista de dict em lista de listas
        tabela = [list(item.values()) for item in resultados]

        return tabulate(tabela, headers=cabecalhos, tablefmt="fancy_grid")





