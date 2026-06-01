from utils.limpar_tela import limpar_tela
from utils.proximo import proximo
from utils.string_vazia import string_vazia
from services import ClienteService

import re

cliente_service = ClienteService()

while True:
    try:
        print("###########################################")
        print("########## FAST DELIVERY EXPRESS ##########")
        print("###########################################\n")

        print("1. Cadastrar clientes")
        print("0. Sair")

        opcao = int(input("Opção: "))

        match opcao:
            case 1:
                while True:
                    limpar_tela()

                    print("Informe os campos a seguir.")

                    cpf = input("Cpf: ")

                    if string_vazia(cpf):
                        print("Cpf não informado.")
                        proximo()
                        continue

                    cpf_regex = r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"
                    cpf_valido = re.search(cpf_regex, cpf)
                    if not cpf_valido:
                        print(
                            "Cpf inválido, ele deve seguir o seguinte padrão: XXX.XXX.XXX-XX."
                        )
                        proximo()
                        continue

                    nome = input("Nome: ")

                    if string_vazia(nome):
                        print("Nome não informado.")
                        proximo()
                        continue

                    telefone = input("Telefone: ")

                    if string_vazia(telefone):
                        print("Telefone não informado.")
                        proximo()
                        continue

                    telefone_regex = r"^\(\d{2}\) \d{4,5}-\d{4}$"
                    telefone_valido = re.search(telefone_regex, telefone)
                    if not telefone_valido:
                        print(
                            "Telefone inválido, ele deve seguir o seguinte formato: (XX) 9XXXX-XXXX."
                        )
                        proximo()
                        continue

                    endereco = input("Endereço: ")
                    if string_vazia(endereco):
                        print("Endereço não informado.")
                        proximo()
                        continue

                    cliente_service.cadastrar(cpf, nome, telefone, endereco)

                    limpar_tela()
                    print("Cliente cadastrado!")
                    proximo()

                    break

            case 0:
                print("Saindo...")
                break

            case _:
                limpar_tela()
                print("Opção inválida, tente novamente")
                proximo()

    except Exception as e:
        limpar_tela()
        print(e)
        proximo()
