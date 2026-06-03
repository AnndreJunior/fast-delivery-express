from interfaces.calculo_frete_interface import CalculoFreteInterface


class CalculoFretePremium(CalculoFreteInterface):
    def calcular_frete(self, distancia: float) -> float:
        return distancia * 5 + 20
