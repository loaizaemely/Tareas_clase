from .cuenta import Cuenta

class CuentaAhorro(Cuenta):
    def __init__(self, numero,titular, saldo=0, interes=0.02):
        super().__init__(numero,titular, saldo)
        self._interes = interes
        self.tipo = "Ahorro"

    def aplicar_interes(self) -> None:
        self._saldo += self._saldo * self._interes
