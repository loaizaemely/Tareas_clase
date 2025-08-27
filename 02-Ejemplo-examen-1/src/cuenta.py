from .cliente import Cliente
class Cuenta:
    def __init__(self, numero: int, titular:Cliente, saldo: float = 0 ):
        self.titular = titular
        self._numero = numero
        self._saldo = saldo

    def depositar(self, monto: float) -> None:
        self._saldo += monto

    def retirar(self, monto: float) -> None:
        if monto <= self._saldo:
            self._saldo -= monto
            print("✅  Retiro exitoso")
        else:
            print("❌  Fondos insuficientes")

    def mostrar_saldo(self) -> str:
        return f"Cuenta {self._numero} - Saldo: {self._saldo}"