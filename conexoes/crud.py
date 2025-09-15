import ctypes
import os
import json
import sys

"""Esse módulo configura a função salvarNoJson que foi escrita em C, para ser reutilizada no
python, na função salvarNoJson abaixo, foi configurada os tipos de argumentos que a função recebe
(argstype) e o tipo de retorno que ela fornece (restype)."""


# detecta o nome certo da biblioteca conforme o SO
if sys.platform.startswith("win"):
    libname = "salvarJson.dll"
elif sys.platform.startswith("linux"):
    libname = "salvarJson.so"
else:
    raise OSError("Sistema operacional não suportado")


lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build", libname))
lib = ctypes.CDLL(lib_path)


def cadastrar(arquivoJson, objeto):

    lib.salvarNoJson.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    lib.salvarNoJson.restype = None
    json_str = json.dumps(objeto)
    lib.salvarNoJson(arquivoJson.encode("utf-8"), json_str.encode("utf-8"))
    print("Produto cadastrado com sucesso")


def consulta(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError as e:
        print(f"Arquivo Json não encontrado {e}")
    except json.JSONDecodeError as e:
        print(f"Nada cadastrado no momento")
        return []









