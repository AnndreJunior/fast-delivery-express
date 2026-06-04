from typing import List
from models import Pedido, PedidoStatus, TipoEntrega, Cliente, Entregador
from interfaces.calculo_frete_interface import CalculoFreteInterface
from .calculo_frete import CalculoFreteComum, CalculoFreteExpresso, CalculoFretePremium

import random
import string


class PedidoService:
    def __init__(self):
        self.__pedidos: List[Pedido] = []

    def cadastrar(
        self,
        cliente: Cliente,
        entregador: Entregador,
        peso: float,
        distancia: float,
        tipo: TipoEntrega,
    ):
        """A distância do pedido a ser entregue é em quilômetros."""
        if peso <= 0:
            raise Exception("O peso do pedido deve ser um número maior que zero.")

        if distancia <= 0:
            raise Exception("A distância da entrega deve ser um número maior que zero.")

        implementacoes_calculo_frete = {
            TipoEntrega.ENTREGA_COMUM: CalculoFreteComum(),
            TipoEntrega.ENTREGA_EXPRESSA: CalculoFreteExpresso(),
            TipoEntrega.ENTREGA_PREMIUM: CalculoFretePremium(),
        }

        calculo_frete: CalculoFreteInterface = implementacoes_calculo_frete[tipo]

        pedido = Pedido(
            self.__gerar_codigo(),
            cliente,
            entregador,
            peso,
            distancia,
            tipo,
            PedidoStatus.PREPARACAO,
            frete=calculo_frete.calcular_frete(distancia),
        )

        self.__pedidos.append(pedido)

    def encontrar_pedido_pelo_codigo(self, codigo: str):
        pedido = next(
            (pedido for pedido in self.__pedidos if pedido.codigo == codigo), None
        )

        if pedido is None:
            raise Exception(f"Pedido de código {codigo} não encontrado.")

        return pedido

    def atualizar_status(self, pedido: Pedido):
        if pedido.status == PedidoStatus.PREPARACAO:
            pedido.status = PedidoStatus.SAIU_PARA_ENTREGA
            return

        if pedido.status == PedidoStatus.SAIU_PARA_ENTREGA:
            pedido.status = PedidoStatus.ENTREGUE
            return

    def cancelar(self, pedido: Pedido):
        if pedido.status == PedidoStatus.ENTREGUE:
            raise Exception(
                "Não é possível cancelar um pedido já entregue. Se necessário, realize a devolução."
            )

        pedido.status = PedidoStatus.CANCELADO

    def listar(self):
        return self.__pedidos

    def __gerar_codigo(self):
        return "".join(random.choices(string.digits, k=8))
