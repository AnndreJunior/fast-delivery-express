from abc import ABC, abstractmethod


class CalculoFreteInterface(ABC):
    @abstractmethod
    def calcular_frete(self, distancia: float) -> float:
        """
        Calcula a distância do frete a depender do tipo de entrega.

        Argumentos:
            distancia (float) - distância em quilômetros.

        Retorn:
            float: o valor total do frete.
        """
        pass
