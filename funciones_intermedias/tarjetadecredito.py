import targetaCredito

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjetas = []

    def agregar_tarjeta(self, tarjeta):
        self.tarjetas.append(tarjeta)
        return self

    def hacer_compra(self, monto, indice_tarjeta):
        print(f"\n{self.nombre} hace una compra de {monto} en la tarjeta #{indice_tarjeta}")
        self.tarjetas[indice_tarjeta].compra(monto)
        return self

    def pagar_tarjeta(self, monto, indice_tarjeta):
        print(f"\n{self.nombre} paga {monto} en la tarjeta #{indice_tarjeta}")
        self.tarjetas[indice_tarjeta].pago(monto)
        return self

    def mostrar_saldo_usuario(self):
        print(f"\n=== Saldo de {self.nombre} ===")
        for i, tarjeta in enumerate(self.tarjetas):
            print(f"\nTarjeta #{i}")
            tarjeta.mostrar_info_tarjeta()
        return self

tarjeta1 = targetaCredito.TarjetaCredito(limite_credito=1000, intereses=3)
tarjeta2 = targetaCredito.TarjetaCredito(limite_credito=500, intereses=7)

maria = Usuario("María")
maria.agregar_tarjeta(tarjeta1).agregar_tarjeta(tarjeta2)

maria.hacer_compra(300, 0).hacer_compra(100, 1).pagar_tarjeta(50, 0).mostrar_saldo_usuario()