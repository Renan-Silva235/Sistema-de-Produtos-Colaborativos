import ctypes
import os
import json

lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build/salvarJson.so"))
lib = ctypes.CDLL(lib_path)


def salvarNoJson(arquivoJson, objeto):

    lib.salvarNoJson.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    lib.salvarNoJson.restype = None
    json_str = json.dumps(objeto)
    lib.salvarNoJson(arquivoJson.encode("utf-8"), json_str.encode("utf-8"))








