from .limpar_tela import limpar_tela
from .proximo import proximo


def exibir_feedback(msg: str, pausar: bool = True):
    """
    Limpa a tela e exibe uma mensagem.

    Argumentos:
        msg (str): A mensagem que será exibida.
        pausar (bool): Se True, aguarda o usuário pressionar Enter. Padrão é True.
    """
    limpar_tela()
    print(msg)
    if pausar:
        proximo()
