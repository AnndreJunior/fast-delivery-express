from utils.limpar_tela import limpar_tela
from utils.proximo import proximo
from utils.string_vazia import string_vazia
from services import ClienteService, EntregadorService, PedidoService
from models import TipoEntrega

import re

cliente_service = ClienteService()
entregador_service = EntregadorService()
pedido_service = PedidoService()

while True:
    try:
        print("###########################################")
        print("########## FAST DELIVERY EXPRESS ##########")
        print("###########################################\n")

        print("1. Cadastrar clientes")
        print("2. Cadastrar entregadores")
        print("3. Cadastrar pedido")
        print("0. Sair")

        opcao = int(input("Opção: "))

        limpar_tela()

        match opcao:
            case 1:
                while True:
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

            case 2:
                while True:
                    print("Informe os campos a seguir.")

                    cnh = input("Número da CNH: ")

                    if string_vazia(cnh):
                        print("Número da CNH não informado.")
                        proximo()
                        continue

                    if len(cnh) != 11:
                        print("O número da CNH deve conter 11 números.")
                        proximo()
                        continue

                    nome = input("Nome: ")

                    if string_vazia(nome):
                        print("Nome do entregador não informado.")
                        proximo()
                        continue

                    veiculo = input("Veículo: ")

                    if string_vazia(veiculo):
                        print("Veículo não informado.")
                        proximo()
                        continue

                    entregador_service.cadastrar(cnh, nome, veiculo)

                    limpar_tela()
                    print("Entregador cadastrado!")
                    proximo()

                    break

            case 3:
                while True:
                    print("Informe os campos relacionados a entrega.")

                    cpf_cliente = input("Informe o CPF do cliente: ")

                    if string_vazia(cpf_cliente):
                        print("Informe o CPF do cliente.")
                        proximo()
                        continue

                    cliente = cliente_service.encontrar_pelo_cpf(cpf_cliente)

                    cnh_entregador = input("Informe a CNH do entregador: ")

                    if string_vazia(cnh_entregador):
                        print("Informe o código da CNH do entregador.")
                        proximo()
                        continue

                    entregador = entregador_service.encontrar_pela_cnh(cnh_entregador)

                    peso = float(input("Peso (kg): "))
                    distancia = float(input("Distância (km): "))

                    print("\nInforme o tipo de entrega.")

                    tipo_entrega_exibicao = {
                        TipoEntrega.ENTREGA_COMUM: "Entrega comum",
                        TipoEntrega.ENTREGA_EXPRESSA: "Entrega expressa",
                        TipoEntrega.ENTREGA_PREMIUM: "Entrega premium",
                    }
                    tipo_entrega_opcoes = {
                        tipo_entrega.value for tipo_entrega in TipoEntrega
                    }

                    for tipo_entrega in TipoEntrega:
                        print(
                            f"{tipo_entrega.value}. {tipo_entrega_exibicao[tipo_entrega]}"
                        )

                    opcao_tipo_de_entrega = int(input("Opção: "))
                    if opcao_tipo_de_entrega not in tipo_entrega_opcoes:
                        print("Opção inválida para o tipo de entrega.")
                        proximo()
                        continue

                    pedido_service.cadastrar(
                        cliente,
                        entregador,
                        peso,
                        distancia,
                        TipoEntrega(opcao_tipo_de_entrega),
                    )

                    limpar_tela()
                    print("Pedido cadastrado!")
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
