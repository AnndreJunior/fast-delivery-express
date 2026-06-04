from utils.string_vazia import string_vazia
from utils.menu import (
    exibir_opcoes_de_entrega,
    limpar_tela,
    proximo,
    exibir_feedback,
    obter_input_valido,
)
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

                cpf = obter_input_valido(
                    prompt="Cpf: ",
                    erro_vazio="Cpf não informado.",
                    regex=r"^\d{3}\.\d{3}\.\d{3}\-\d{2}$",
                    erro_regex="Cpf inválido, ele deve seguir o seguinte padrão: XXX.XXX.XXX-XX.",
                )

                nome = obter_input_valido(
                    prompt="Nome: ", erro_vazio="Nome não informado."
                )

                telefone = obter_input_valido(
                    prompt="Telefone: ",
                    erro_vazio="Telefone não informado.",
                    regex=r"^\(\d{2}\) \d{4,5}-\d{4}$",
                    erro_regex="Telefone inválido, ele deve seguir o seguinte formato: (XX) 9XXXX-XXXX.",
                )

                endereco = obter_input_valido(
                    prompt="Endereço: ", erro_vazio="Endereço não informado."
                )

                cliente_service.cadastrar(cpf, nome, telefone, endereco)

                exibir_feedback("Cliente cadastrado!")

            case 2:
                print("Informe os campos a seguir.")

                while True:
                    cnh = obter_input_valido(
                        prompt="Número da CNH: ",
                        erro_vazio="Número da CNH não informado.",
                    )

                    if len(cnh) != 11:
                        exibir_feedback(
                            "O número da CNH deve conter 11 números.", pausar=False
                        )
                        continue
                    break

                nome = obter_input_valido(
                    prompt="Nome: ", erro_vazio="Nome do entregador não informado."
                )

                veiculo = obter_input_valido("Veículo: ", "Veículo não informado.")

                entregador_service.cadastrar(cnh, nome, veiculo)

                exibir_feedback("Entregador cadastrado!")

            case 3:
                print("Informe os campos relacionados a entrega.")

                cpf_cliente = obter_input_valido(
                    prompt="Informe o CPF do cliente: ",
                    erro_vazio="CPF do cliente não informado.",
                )

                cliente = cliente_service.encontrar_pelo_cpf(cpf_cliente)

                cnh_entregador = obter_input_valido(
                    prompt="Informe a CNH do entregador: ",
                    erro_vazio="CNH do entregador não informado.",
                )

                entregador = entregador_service.encontrar_pela_cnh(cnh_entregador)

                peso = float(
                    obter_input_valido(
                        prompt="Peso (kg): ",
                        erro_vazio="Peso da entrega não informado.",
                    )
                )
                distancia = float(
                    obter_input_valido(
                        prompt="Distância (km): ",
                        erro_vazio="Distância da entrega não informada.",
                    )
                )

                print("\nInforme o tipo de entrega.")

                tipo_entrega_opcoes = {
                    tipo_entrega.value for tipo_entrega in TipoEntrega
                }

                while True:
                    exibir_opcoes_de_entrega()
                    opcao_str = input("Opção: ")

                    if string_vazia(opcao_str):
                        exibir_feedback("Tipo de entrega não informada.", pausar=False)
                        continue

                    opcao_tipo_de_entrega = int(opcao_str)

                    if opcao_tipo_de_entrega not in tipo_entrega_opcoes:
                        exibir_feedback(
                            "Opção inválida para o tipo de entrega. Informe um valor correspondente.",
                            pausar=False,
                        )
                        continue
                    break

                pedido_service.cadastrar(
                    cliente,
                    entregador,
                    peso,
                    distancia,
                    TipoEntrega(opcao_tipo_de_entrega),
                )

                exibir_feedback("Pedido cadastrado!")

            case 4:
                status_exibicao = {
                    PedidoStatus.SAIU_PARA_ENTREGA: "Saiu para entrega",
                    PedidoStatus.PREPARACAO: "Em preparação",
                    PedidoStatus.ENTREGUE: "Entregue",
                    PedidoStatus.CANCELADO: "Cancelado",
                }
                pedidos = pedido_service.listar()

                if not pedidos:
                    exibir_feedback("Nenhum pedido cadastrado.")
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
                codigo = obter_input_valido(
                    prompt="Código do pedido: ",
                    erro_vazio="Informe o código do pedido.",
                )

                pedido = pedido_service.encontrar_pedido_pelo_codigo(codigo)

                limpar_tela()

                while True:
                    print("Deseja atualizar a situação ou cancelar?")
                    print("1. Atualizar")
                    print("2. Cancelar")

                    opcao_str = input("Opção: ")

                    if string_vazia(opcao_str):
                        exibir_feedback(
                            "Informe se você deseja atualizar ou cancelar o pedido.",
                            pausar=False,
                        )
                        continue

                    opcao = int(opcao_str)

                    limpar_tela()

                    if opcao == 1:
                        pedido_service.atualizar_status(pedido)
                        print(f"Situação do pedido {codigo} atualizado com sucesso!")
                        print(f"Situação atual: {status_exibicao[pedido.status]}.")
                    elif opcao == 2:
                        pedido_service.cancelar(pedido)
                        print(f"Pedido {codigo} cancelado.")
                    else:
                        exibir_feedback("Opção inválida.", pausar=False)
                        continue
                    break

                proximo()

            case 0:
                print("Saindo...")
                break

            case _:
                exibir_feedback("Opção inválida, tente novamente.")

    except Exception as e:
        exibir_feedback(f"{e}")
