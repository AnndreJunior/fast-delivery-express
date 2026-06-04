from utils.string_vazia import string_vazia
from utils.checar_padrao import padrao_valido
from .exibir_feedback import exibir_feedback


def obter_input_valido(
    prompt: str,
    erro_vazio: str,
    regex: str | None = None,
    erro_regex: str | None = None,
) -> str:
    """Solicita um input ao usuário em loop até que seja válido."""
    while True:
        valor = input(prompt)

        if string_vazia(valor):
            exibir_feedback(erro_vazio, pausar=False)
            continue

        if regex and not padrao_valido(valor, regex):
            exibir_feedback(
                erro_regex or "Padrão inválido. Tente novamente.", pausar=False
            )
            continue

        return valor
