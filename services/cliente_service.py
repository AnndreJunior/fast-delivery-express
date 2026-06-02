from typing import List
from models import Cliente


class ClienteService:
    def __init__(self):
        self.__clientes: List[Cliente] = []

    def cadastrar(self, cpf: str, nome: str, telefone: str, endereco: str):
        cpf_ja_cadastrado = next(
            (cliente for cliente in self.__clientes if cliente.cpf == cpf), None
        )

        if cpf_ja_cadastrado:
            raise Exception(f"Usuário com CPF {cpf} já cadastrado.")

        cliente = Cliente(nome, cpf, telefone, endereco)
        self.__clientes.append(cliente)

    def encontrar_pelo_cpf(self, cpf: str):
        cliente = next(
            (cliente for cliente in self.__clientes if cliente.cpf == cpf), None
        )

        if cliente is None:
            raise Exception(f"Cliente com cpf {cpf} não foi cadastrado.")

        return cliente
