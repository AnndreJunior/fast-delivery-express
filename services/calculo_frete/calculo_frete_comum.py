from interfaces.calculo_frete_interface import CalculoFreteInterface


class CalculoFreteComum(CalculoFreteInterface):
    def calcular_frete(self, distancia: float) -> float:
        return distancia * 1.5
