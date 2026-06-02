from typing import List
from models import Pedido, PedidoStatus, Cliente, Entregador

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
        tipo: str,
    ):
        """A distância do pedido a ser entregue é em quilômetros."""
        if peso <= 0:
            raise Exception("O peso do pedido deve ser um número maior que zero.")

        if distancia <= 0:
            raise Exception("A distância da entrega deve ser um número maior que zero.")

        pedido = Pedido(
            self.__gerar_codigo(),
            cliente,
            entregador,
            peso,
            distancia,
            tipo,
            PedidoStatus.PREPARACAO,
        )

        self.__pedidos.append(pedido)
        pass

    def __gerar_codigo(self):
        return "".join(random.choices(string.digits, k=8))
