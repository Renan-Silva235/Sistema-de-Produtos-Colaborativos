import json
import os
import sys
import ctypes
class Crud:
    def __init__(self, arquivo):
        self.json = arquivo

    def consultar(self, dado):
        """
        Realiza uma consulta nos dados salvos no json

        :param dado: O valor que deve ser  procurado no json
        :return: Uma lista com os objetos que contenham o valor procurado
        """
        lista = self.listar()
        resultados = []

        for item in lista:
            if any(str(dado).lower() in str(valor).lower() for valor in item.values()):
                resultados.append(item)

        if not resultados:
            return False

        return resultados

    def listar(self):
        """
        Retorna uma lista com todos os objetos salvos no json.

        :return: Uma lista com todos os objetos salvos no json
        """
        if os.path.exists(self.json):
            with open(self.json, "r", encoding="utf-8") as arq:
                conteudo = arq.read().strip()
                if not conteudo:
                    return []
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

        json_str = json.dumps(dados)
        lib.salvarNoJson(self.json.encode("utf-8"), json_str.encode("utf-8"))


    def atualizar(self, id_produto, chave, novo_valor):
        """
        Atualiza o valor de uma chave em um produto específico (pelo ID).
        """
        dados = self.listar()
        for dado in dados:
            if dado["id"] == id_produto:
                dado[chave] = novo_valor
                break  # para após atualizar o produto certo

        with open(self.json, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

