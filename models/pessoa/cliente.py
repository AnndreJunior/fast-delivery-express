from .pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, telefone: str, endereco: str):
        super().__init__(nome)

        self.__cpf = cpf
        self.__telefone = telefone
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @property
    def telefone(self):
        return self.__telefone

    @property
    def endereco(self):
        return self.__endereco
