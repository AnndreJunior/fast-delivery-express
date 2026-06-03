from interfaces.calculo_frete_interface import CalculoFreteInterface


class CalculoFreteExpresso(CalculoFreteInterface):
    def calcular_frete(self, distancia: float) -> float:
        return distancia * 3
