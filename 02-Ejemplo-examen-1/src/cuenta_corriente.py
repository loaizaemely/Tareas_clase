from .cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, numero,titular, saldo=0, sobregiro=500):
        super().__init__(numero,titular, saldo)
        self._sobregiro = sobregiro
        self.tipo = "Corriente"

    def retirar(self, monto: float) -> None:
        if monto <= self._saldo + self._sobregiro:
            self._saldo -= monto
            print("✅  Retiro exitoso Cuenta Corriente")
        else:
            print("❌  Límite de sobregiro excedido")
        