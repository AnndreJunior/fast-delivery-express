from typing import List
from models.entregador import Entregador


class EntregadorService:
    def __init__(self):
        self.__entregadores: List[Entregador] = []

    def cadastrar(self, cnh: str, nome: str, veiculo: str):
        cnh_cadastrada = next(
            (entregador for entregador in self.__entregadores if entregador.cnh == cnh),
            None,
        )

        if cnh_cadastrada:
            raise Exception(f"Entregador com a cnh {cnh} já cadastrado.")

        entregador = Entregador(nome, veiculo, cnh)
        self.__entregadores.append(entregador)

    def encontrar_pela_cnh(self, cnh: str):
        entregador = next(
            (entregador for entregador in self.__entregadores if entregador.cnh == cnh),
            None,
        )

        if entregador is None:
            raise Exception(f"O entregador com a CNH {cnh} não está cadastrado.")

        return entregador
