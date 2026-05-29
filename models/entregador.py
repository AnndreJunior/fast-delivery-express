from .pessoa import Pessoa


class Entregador(Pessoa):
    def __init__(self, nome: str, veiculo: str, cnh: str):
        super().__init__(nome)

        self.__veiculo = veiculo
        self.__cnh = cnh

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def cnh(self):
        return self.__cnh
