def string_vazia(valor: str):
    """
    Verifica se um valor do tipo texto é vazio.

    Argumentos:
        valor (str)

    Retorno:
        bool: verdadeiro caso o valor esteja vazio, caso contrário falso
    """
    return valor is None or len(valor) == 0
