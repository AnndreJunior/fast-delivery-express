from models import TipoEntrega


def exibir_opcoes_de_entrega():
    tipo_entrega_exibicao = {
        TipoEntrega.ENTREGA_COMUM: "Entrega comum",
        TipoEntrega.ENTREGA_EXPRESSA: "Entrega expressa",
        TipoEntrega.ENTREGA_PREMIUM: "Entrega premium",
    }
    for tipo_entrega in TipoEntrega:
        print(f"{tipo_entrega.value}. {tipo_entrega_exibicao[tipo_entrega]}")
