import json
from crud.crud import Crud
class Alteracoes:


    def alterar_estoque(self, caminho_arquivo, produto_id, quantidade_alterar):
        """
        Altera a quantidade de um produto no estoque.

        :param caminho_arquivo: O caminho do arquivo json que contém o estoque.
        :param produto_id: O id do produto que vai ser alterado.
        :param quantidade_alterar: A quantidade a ser alterada no produto.
        :return: True se a quantidade for alterada, False caso contrário.
        """
        consulta = Crud(caminho_arquivo).listar()

        if not consulta:
            return False


        atualizado = False
        for item in consulta:
            if item.get("id") == produto_id:
                item["quantidade"] = item.get("quantidade", 0) + quantidade_alterar
                atualizado = True
                break

        if atualizado:
            with open(caminho_arquivo, "w") as arquivo:
                json.dump(consulta, arquivo, indent=4, ensure_ascii=False)
        else:
            return False


    def alterar_total_doacoes(self,cpf, quantidade):
        """Esse método atualiza o número de doações feitas pelo usuário somando o que ele já havia doado pela
        quantidade total de produtos que ele está doando no momento."""

        todos_doadores = Crud("jsons/dados_pessoais/doadores.json").listar()

        atualizado = False
        for doador in todos_doadores:
            if doador["cpf"] == cpf:
                doador["total_doacoes"] = doador["total_doacoes"] + quantidade
                atualizado = True
                break

        if atualizado:
            with open("jsons/dados_pessoais/doadores.json", "w") as arquivo:
                json.dump(todos_doadores, arquivo, indent=4, ensure_ascii=False)
        else:
            return False


    def alterar_produto_existente(self, caminho_arquivo, id_produto, quantidade, id_doador):
        """Atualiza quantidade e adiciona o id do doador no produto já existente."""

        consulta = Crud(caminho_arquivo).listar()

        for item in consulta:
            if item["id"] == id_produto:
                # soma quantidade
                item["quantidade"] += quantidade

                # garante que id_doadores exista
                if "id_doador" not in item:
                    item["id_doador"] = []

                # adiciona o doador se ainda não estiver
                if id_doador not in item["id_doador"]:
                    item["id_doador"].append(id_doador)

                break

        """Esse bloco de código abaixo faz uma pequenha formatação na hora de salvar o id do usuário
        já que a biblioteca json não faz isso automaticamente quando se adiciona algum item em uma lista no json."""
        partes = []
        for item in consulta:
            # tira id_doadores temporariamente
            id_doadores = item.pop("id_doador", [])
            # serializa o resto normalmente
            base = json.dumps(item, indent=4, ensure_ascii=False)
            base = base.rstrip(" \n}")  # remove } e quebras no fim
            # serializa id_doadores em linha
            id_doadores_str = json.dumps(id_doadores, separators=(",", ":"))
            # junta tudo de volta
            final = f"{base},\n    \"id_doador\": {id_doadores_str}\n    }}"
            partes.append(final)

        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write("[\n" + ",\n".join(partes) + "\n]")


    def alterar_validade_produto(self, caminho_arquivo, produto_id, nova_validade):
        """
        Altera a validade de um produto específico pelo ID.

        :param caminho_arquivo: O caminho do arquivo json que contém o estoque.
        :param produto_id: O id do produto que vai ser alterado.
        :param nova_validade: A nova validade no formato dd/mm/aaaa.
        :return: True se a validade for alterada, False caso contrário.
        """
        itens = Crud(caminho_arquivo).listar()

        if not itens:
            return False

        # Busca e atualiza apenas o produto com o ID específico
        for item in itens:
            if item.get("id") == produto_id:
                item["validade"] = nova_validade
                # Salva o arquivo atualizado
                with open(caminho_arquivo, "w") as arquivo:
                    json.dump(itens, arquivo, indent=4, ensure_ascii=False)
                return True

        return False


    def alterar_status_produto(self, caminho_arquivo, produto_id, novo_status):
        """
        Altera o status de um produto específico pelo ID.

        :param caminho_arquivo: O caminho do arquivo json que contém o estoque.
        :param produto_id: O id do produto que vai ser alterado.
        :param novo_status: O novo status ("ativo" ou "inativo").
        :return: True se o status for alterado, False caso contrário.
        """
        itens = Crud(caminho_arquivo).listar()

        if not itens:
            return False

        # Busca e atualiza apenas o produto com o ID específico
        for item in itens:
            if item.get("id") == produto_id:
                item["status"] = novo_status
                # Salva o arquivo atualizado
                with open(caminho_arquivo, "w") as arquivo:
                    json.dump(itens, arquivo, indent=4, ensure_ascii=False)
                return True

        return False


