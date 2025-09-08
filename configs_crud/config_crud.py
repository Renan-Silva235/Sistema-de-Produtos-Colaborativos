import ctypes
import os
import json



class Crud:

    def __init__(self):
        self.lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build/libcrud.so"))
        self.lib = ctypes.CDLL(self.lib_path)


    def cadastrar(self, arquivoJson, objeto):

        self.lib.cadastrar.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.lib.cadastrar.restype = None
        json_str = json.dumps(objeto)
        self.lib.cadastrar(arquivoJson.encode("utf-8"), json_str.encode("utf-8"))








