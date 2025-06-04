#Aileen Jara 
#29-05

class TarjetaCredito:

    tarjetas = []


    def __init__(self, saldo_pagar=0, limite_credito=100000, intereses=0.02):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.tarjetas.append(self)

    def comprar(self, monto):
        if self.saldo_pagar + monto <=self.limite_credito:
            self.saldo_pagar += monto
            print(f"Compra realizada:${monto:,}. Nuevo saldo:${self.saldo_pagar:,}")
        else:
            print("Tarjeta Rechazada, haz alcanzado tu limte de credito.")
        return self
    def pago(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar =0
        print(f"Pago Realizado:${monto:,} Nuevo saldo: ${self.saldo_pagar:,}")
        return self
    
    def mostrar_info_tarjeta(self):
        print("-------Infromacion de la Tarjeta-------")
        print(f"Saldo a Pagar: ${self.saldo:,}")
        print(f"Limite de Credito:{self.limite_credito}:,")
        return self
    
    def cobrar_intereses(self):
        self.saldo_pagar+= self.saldo_pagar *self.intereses
        print(f"Ineteres cobrado. Nuevo saldo:${self.saldo_pagar:,.2f}")
        return self
    @classmethod
    def mostrar_todas_tarjetas(cls):
        for i, tarjeta in enumerate(cls.tarjeta, 1):
            print(f"Tarjeta {i: Saldo:${tarjeta.saldo_pagar:,}, Limite:${tarjeta.limite_credito:,}, Intereses:{tarjeta.intereses:,.2%}}")

print("======= Tarjeta 1 =======")
tarjeta1 = TarjetaCredito()
tarjeta1.comprar(500000).comprar(20000).pago(10000).cobrar_intereses().mostrar_info_tarjeta

print("=================================================")

print("======= Tarjeta 2 =======")
tarjeta2 = TarjetaCredito(limite_credito=300000, intereses=0.015)
tarjeta2.comprar(700000).comprar(50000).pago(40000).cobrar_intereses().mostrar_info_tarjeta

print("=================================================")

print("======= Tarjeta 3 =======")
tarjeta3 = TarjetaCredito(limite_credito=100000, intereses=0.02)
tarjeta3.comprar(700000).comprar(50000).pago(40000).cobrar_intereses().mostrar_info_tarjeta

print("=================================================")


# tarjeta1 = TarjetaCredito(limite_credito=200000, intereses=0.02)
# tarjeta1.comprar(50000) 
# tarjeta1.pagar(3000)
# tarjeta1.mostrar_info_tarjeta()
# tarjeta1.cobrar_intereses()