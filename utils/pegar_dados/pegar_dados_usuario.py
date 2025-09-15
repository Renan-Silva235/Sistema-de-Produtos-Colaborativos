from utils.sistema.sistema import limpar_tela
import time
from validacoes.validacao import Validacoes


def pegar_dados_doadores():
    try:
        nome = input("Digite seu nome: ").title()
        sobrenome = input("Digite seu sobrenome: ").title()
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite o seu CPF: ")
        cidade = input("Digite a sua cidade: ").title()
        estado = input("Digite o seu estado: ").title()
        email = input("Digite seu email: ").lower()
        telefone = input("Digite o seu telefone: ")
    except ValueError:
        print("Tipo de dado inválido")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_campos(nome, sobrenome, cidade, estado, cpf, email, telefone):
        print("Nenhum campo pode estar vazio")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_email(email):
        print("E-mail inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_cpf(cpf):
        print("CPF inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_nome(nome):
        print("Nome inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_nome(sobrenome):
        print("sobrenome inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_cpf(cpf):
        print("CPF inválido.")
        time.sleep(1)
        limpar_tela()
        return False


    return     {
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade,
        "cpf": cpf,
        "cidade": cidade,
        "estado": estado,
        "email": email,
        "telefone": telefone,
        "total_doacoes": 0
    }



def pegar_dados_solicitantes():
    try:
        nome = input("Digite seu nome: ").title()
        sobrenome = input("Digite seu sobrenome: ").title()
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite o seu CPF: ")
        cidade = input("Digite a sua cidade: ").title()
        estado = input("Digite o seu estado: ").title()
        telefone = input("Digite o seu telefone: ")
        email = input("Digite seu email: ").lower()
        senha = input("Crie uma senha de 4 dígitos numérica: ")
        redigitar_senha = input("Digite a sua senha novamente: ")
    except ValueError:
        print("Tipo de dado inválido")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_campos(nome, sobrenome, cidade, estado, cpf, email, telefone):
        print("Nenhum campo pode estar vazio")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_email(email):
        print("E-mail inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_cpf(cpf):
        print("CPF inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_nome(nome):
        print("Nome inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_nome(sobrenome):
        print("sobrenome inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_cpf(cpf):
        print("CPF inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_senha(senha):
        print("Senha inválida")
        time.sleep(1)
        limpar_tela()
        return False

    if redigitar_senha != senha:
        print("Senha não coincidem")
        time.sleep(1)
        limpar_tela()
        return False



    return     {
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade,
        "cpf": cpf,
        "cidade": cidade,
        "estado": estado,
        "telefone": telefone,
        "email": email,
        "senha": senha
    }



def pegar_dados_voluntario():
    try:
        nome = input("Digite seu nome: ").title()
        sobrenome = input("Digite seu sobrenome: ").title()
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite o seu CPF: ")
        cargo = input("Digite o cargo: ").title()
        telefone = input("Digite o seu telefone: ")
        email = input("Digite seu email: ").lower()
        senha = input("Crie uma senha de 4 dígitos numérica: ")
        redigitar_senha = input("Digite a sua senha novamente: ")
    except ValueError:
        print("Tipo de dado inválido")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_campos(nome, sobrenome, cpf, email, telefone):
        print("Nenhum campo pode estar vazio")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_email(email):
        print("E-mail inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_cpf(cpf):
        print("CPF inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_nome(nome):
        print("Nome inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_nome(sobrenome):
        print("sobrenome inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_cpf(cpf):
        print("CPF inválido.")
        time.sleep(1)
        limpar_tela()
        return False

    if not Validacoes.validar_senha(senha):
        print("Senha inválida")
        time.sleep(1)
        limpar_tela()
        return False

    if redigitar_senha != senha:
        print("Senha não coincidem")
        time.sleep(1)
        limpar_tela()
        return False



    return {
        "nivel": None,
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade,
        "cpf": cpf,
        "cargo": cargo,
        "telefone": telefone,
        "email": email,
        "senha": senha
    }
