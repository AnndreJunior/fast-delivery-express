from utils.string_vazia import string_vazia
from utils.menu import exibir_opcoes_de_entrega, limpar_tela, proximo
from utils.checar_padrao import padrao_valido
from services import ClienteService, EntregadorService, PedidoService
from models import TipoEntrega, PedidoStatus

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
        print("4. Atualizar pedido")
        print("0. Sair")

        opcao = int(input("Opção: "))

        limpar_tela()

        match opcao:
            case 1:
                print("Informe os campos a seguir.")

                while True:
                    cpf = input("Cpf: ")

                    if string_vazia(cpf):
                        limpar_tela()
                        print("Cpf não informado.")
                        continue

                    if not padrao_valido(
                        valor=cpf, padrao=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$"
                    ):
                        limpar_tela()
                        print(
                            "Cpf inválido, ele deve seguir o seguinte padrão: XXX.XXX.XXX-XX."
                        )
                        continue
                    break

                while True:
                    nome = input("Nome: ")

                    if string_vazia(nome):
                        limpar_tela()
                        print("Nome não informado.")
                        continue
                    break

                while True:
                    telefone = input("Telefone: ")

                    if string_vazia(telefone):
                        limpar_tela()
                        print("Telefone não informado.")
                        continue

                    if not padrao_valido(
                        valor=telefone, padrao=r"^\(\d{2}\) \d{4,5}-\d{4}$"
                    ):
                        limpar_tela()
                        print(
                            "Telefone inválido, ele deve seguir o seguinte formato: (XX) 9XXXX-XXXX."
                        )
                        continue
                    break

                while True:
                    endereco = input("Endereço: ")
                    if string_vazia(endereco):
                        limpar_tela()
                        print("Endereço não informado.")
                        continue
                    break

                cliente_service.cadastrar(cpf, nome, telefone, endereco)

                limpar_tela()
                print("Cliente cadastrado!")
                proximo()

            case 2:
                print("Informe os campos a seguir.")

                while True:
                    cnh = input("Número da CNH: ")

                    if string_vazia(cnh):
                        limpar_tela()
                        print("Número da CNH não informado.")
                        continue

                    if len(cnh) != 11:
                        limpar_tela()
                        print("O número da CNH deve conter 11 números.")
                        continue
                    break

                while True:
                    nome = input("Nome: ")

                    if string_vazia(nome):
                        limpar_tela()
                        print("Nome do entregador não informado.")
                        continue
                    break

                while True:
                    veiculo = input("Veículo: ")

                    if string_vazia(veiculo):
                        limpar_tela()
                        print("Veículo não informado.")
                        continue
                    break

                entregador_service.cadastrar(cnh, nome, veiculo)

                limpar_tela()
                print("Entregador cadastrado!")
                proximo()

            case 3:
                print("Informe os campos relacionados a entrega.")

                while True:
                    cpf_cliente = input("Informe o CPF do cliente: ")

                    if string_vazia(cpf_cliente):
                        limpar_tela()
                        print("Informe o CPF do cliente.")
                        continue
                    break

                cliente = cliente_service.encontrar_pelo_cpf(cpf_cliente)

                while True:
                    cnh_entregador = input("Informe a CNH do entregador: ")

                    if string_vazia(cnh_entregador):
                        limpar_tela()
                        print("Informe o código da CNH do entregador.")
                        continue
                    break

                entregador = entregador_service.encontrar_pela_cnh(cnh_entregador)

                peso = float(input("Peso (kg): "))
                distancia = float(input("Distância (km): "))

                print("\nInforme o tipo de entrega.")

                tipo_entrega_opcoes = {
                    tipo_entrega.value for tipo_entrega in TipoEntrega
                }

                exibir_opcoes_de_entrega()

                while True:
                    opcao_tipo_de_entrega = int(input("Opção: "))
                    if opcao_tipo_de_entrega not in tipo_entrega_opcoes:
                        limpar_tela()
                        print(
                            "Opção inválida para o tipo de entrega. Informe um valor correspondente."
                        )
                        exibir_opcoes_de_entrega()
                        continue
                    break

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

            case 4:
                status_exibicao = {
                    PedidoStatus.SAIU_PARA_ENTREGA: "Saiu para entrega",
                    PedidoStatus.PREPARACAO: "Em preparação",
                    PedidoStatus.ENTREGUE: "Entregue",
                    PedidoStatus.CANCELADO: "Cancelado",
                }
                pedidos = pedido_service.listar()

                if not pedidos:
                    print("Nenhum pedido cadastrado.")
                    proximo()
                    continue

                for pedido in pedidos:
                    print(f"Código: {pedido.codigo}")
                    print(f"Peso: {pedido.peso} kg")
                    print(f"Distância: {pedido.distancia} km")
                    print(f"Frete: R${pedido.frete}")
                    print(f"Situação: {status_exibicao[pedido.status]}")
                    print(
                        "--------------------------------------------------------------"
                    )

                print("")
                while True:
                    codigo = input("Código do pedido: ")
                    if string_vazia(codigo):
                        print("Informe o código do pedido.")
                        continue
                    break

                pedido = pedido_service.encontrar_pedido_pelo_codigo(codigo)

                limpar_tela()

                while True:
                    print("Deseja atualizar a situação ou cancelar?")
                    print("1. Atualizar")
                    print("2. Cancelar")
                    opcao = int(input("Opção: "))

                    limpar_tela()

                    if opcao == 1:
                        pedido_service.atualizar_status(pedido)
                        print(f"Situação do pedido {codigo} atualizado com sucesso!")
                        print(f"Situação atual: {status_exibicao[pedido.status]}.")
                    elif opcao == 2:
                        pedido_service.cancelar(pedido)
                        print(f"Pedido {codigo} cancelado.")
                    else:
                        print("Opção inválida.")
                        continue
                    break

                proximo()

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
