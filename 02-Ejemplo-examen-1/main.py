from src.cuenta_ahorro import CuentaAhorro
from src.cuenta_corriente import CuentaCorriente
from src.cliente import Cliente


def validar_datos(documento, numero, nombre):#funcion que verifica si un numero es del tipo indicado
    # Validar números
    if not (documento.isdigit() and numero.isdigit()):
        print("❌  Ingrese un dato numérico en documento y número de cuenta")
        return False
    
    # Validar nombre
    if not (nombre.isalpha()):
        print("❌  Ingrese un dato alfabético en el nombre")
        return False
        
    return True

def menu():
    print("\n🪙🪙🪙🪙  BANCO 🪙🪙🪙🪙")
    print("1. 🏦 Crear cuenta de ahorro")
    print("2. 🏦 Crear cuenta corriente")
    print("3. 🔽 Depositar")
    print("4. 🔼 Retirar")
    print("5. 💵 Mostrar saldo")
    print("6. 🔶 Mostrar cuentas")
    print("7. ➡️  Salir")
    
def main() -> None:
    cuentas = {} # Diccionario para almacenar cuentas
    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:#Crear cuenta de ahorro
            nombre = input("Nombre del titular: ")
            documento = input("Documento del titular: ")
            numero = input("Número de cuenta: ")
            persona = Cliente(nombre, documento)
            if validar_datos(documento, numero, nombre):
                cuentas[numero] = CuentaAhorro(numero, persona)
                print("✅  Cuenta de ahorro creada.")
            else:
                print("❌  DATOS NO VALIDOS")
                continue

        elif opcion == 2:# Crear cuenta corriente
            nombre = input("Nombre del titular: ")
            documento = input("Documento del titular: ")
            numero = input("Número de cuenta: ")
            persona = Cliente(nombre, documento)
            if validar_datos(documento, numero, nombre):
                cuentas[numero] = CuentaCorriente(numero, persona)
                print("✅  Cuenta de ahorro creada.")
            else:
                print("❌  DATOS NO VALIDOS")
                continue            
        elif opcion == 3:#Depositar
            if cuentas == {}:
                print("❕No hay cuentas creadas, cree una cuenta primero")
                continue
            monto = float(input("🪙  Monto: "))
            numero = input("Número de cuenta: ")
            if numero in cuentas:
                cuentas[numero].depositar(monto)
                print("🪙🪙  Monto depositado exitosamente. 🪙🪙")
            else:
                print("❌  Cuenta no encontrada.")
        elif opcion == 4:#Retirar
            if cuentas == {}:
                print("❕No hay cuentas creadas, cree una cuenta primero")
                continue
            monto = float(input("🪙Monto: "))
            numero = input("Número de cuenta: ")
            if numero in cuentas:
                if cuentas[numero].tipo == "Ahorro":
                    cuentas[numero].retirar(monto)
                else:
                    cuentas[numero].retirar(monto)
            else:
                print("❌  Cuenta no encontrada.")
        elif opcion == 5:#Mostrar saldo
            if cuentas == {}:
                print("❕No hay cuentas creadas, cree una cuenta primero")
                continue
            numero = input("Número de cuenta: ")
            if numero in cuentas:
                print(cuentas[numero].mostrar_saldo())
            else:
                print("❌  Cuenta no encontrada.")
            
        elif opcion == 6:#Mostrar cuentas
            if cuentas == {}:
                print("❕No hay cuentas creadas, cree una cuenta primero")
                continue
            print("🔸🔸🔸🔸 CUENTAS DISPONIBLES: 🔸🔸🔸🔸")
            for v in cuentas.values():
                print( f"Titular: {v.titular.nombre}\nDocumento: {v.titular.documento}\n{v.mostrar_saldo()}\nTipo de cuenta: {v.tipo}\n🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸")
        elif opcion == 7:#Salir
            print("➡️  Saliendo...")
            break
        else:
            print("❌  Opción no válida.")


# condicional para ejecutar el main, cuando se corre el archivo directamente
if __name__ == "__main__":
    main()
