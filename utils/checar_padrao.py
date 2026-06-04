import re


def padrao_valido(valor: str, padrao: str):
    """
    Checa se o valor informado segue determinado padrão.

    Argumentos:
        valor (str): valor que será verificado
        padrao (str): regex representando o padrão

    Retorno:
        bool: verdadeiro se seguir o padrão. Caso contrário falso
    """
    return re.search(padrao, valor) is not None
