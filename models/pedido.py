from enum import Enum
from .cliente import Cliente
from .entregador import Entregador


class PedidoStatus(Enum):
    PREPARACAO = 1
    SAIU_PARA_ENTREGA = 2
    ENTREGUE = 3
    CANCELADO = 4


class TipoEntrega(Enum):
    ENTREGA_COMUM = 1
    ENTREGA_EXPRESSA = 2
    ENTREGA_PREMIUM = 3


class Pedido:
    def __init__(
        self,
        codigo: str,
        cliente: Cliente,
        entregador: Entregador,
        peso: float,
        distancia: float,
        tipo_entrega: TipoEntrega,
        status: PedidoStatus,
        frete: float,
    ):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__entregador = entregador
        self.__peso = peso
        self.__distancia = distancia
        self.__tipo_entrega = tipo_entrega
        self.__status = status
        self.__frete = frete

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def entregador(self):
        return self.__entregador

    @property
    def peso(self):
        return self.__peso

    @property
    def distancia(self):
        return self.__distancia

    @property
    def tipo_entrega(self):
        return self.__tipo_entrega

    @property
    def status(self):
        return self.__status

    @property
    def frete(self):
        return self.__frete

    @status.setter
    def status(self, status: PedidoStatus):
        self.__status = status
