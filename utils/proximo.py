from .limpar_tela import limpar_tela


def proximo():
    """
    Pausa a execução aguardando o usuário apertar 'Enter' e, em seguida, limpa a tela.

    Utilizada para dar tempo ao usuário de ler mensagens de erro ou sucesso
    antes de retornar ao menu ou prosseguir para a próxima etapa.
    """
    input("Aperte enter para continuar...")
    limpar_tela()
