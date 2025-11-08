import json
import os
import sys
import ctypes


class Crud:
    """
    Classe responsável por operações CRUD (Create, Read, Update, Delete) em arquivos JSON.

    Fornece métodos para listar, consultar, cadastrar e atualizar dados armazenados em arquivos JSON.
    Utiliza uma biblioteca em C compilada (salvarJson.dll/.so) para salvar dados.
    """

    def __init__(self, arquivo):
        """
        Inicializa um objeto Crud com o caminho do arquivo JSON a ser manipulado.

        :param arquivo: String com o caminho do arquivo JSON
        """
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
        """
        Cadastra novos dados no arquivo JSON utilizando uma biblioteca compilada em C.

        Este método configura a função salvarNoJson escrita em C para ser utilizada em Python.
        Os tipos de argumentos (argstype) e o tipo de retorno (restype) são configurados
        para garantir compatibilidade entre Python e C.

        :param dados: Dicionário com os dados a serem cadastrados no JSON
        :return: None
        :raises OSError: Se o sistema operacional não for suportado (Windows ou Linux)
        """

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
        Atualiza o valor de uma chave em um item específico do JSON pelo ID.

        :param id_produto: Inteiro com o ID do item a ser atualizado
        :param chave: String com o nome da chave a ser atualizada
        :param novo_valor: Novo valor a ser atribuído à chave
        :return: None
        """
        dados = self.listar()
        for dado in dados:
            if dado["id"] == id_produto:
                dado[chave] = novo_valor
                break  # para após atualizar o produto certo

        with open(self.json, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

