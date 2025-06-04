#Aileen Jara 
#26-05
from TarjetaCredito import TarjetaCredito


class usuario:
     def __init__(self, nombre, apellido, email):
          self.nombre = nombre
          self.apellido = apellido 
          self.email = email
          self.limite_credito =30000
          self.saldo_pagar = 0

     def agregar_tarjeta(self, tarjeta):
        """Agrega una nueva tarjeta al usuario."""
        self.tarjetas.append(tarjeta)
        print(f"Tarjeta agregada al usuario{self.nombre}. Ahora tiene {len(self.tarjetas)} tarjetas(s).")


     def hacer_compra(self, monto, indice_tarjeta=0):
      """Realiza una compra en la tarjeta especificada (por indice)"""
      if 0<= indice_tarjeta < len(self.tarjetas):
          self.tarjetas[indice_tarjeta].pago(monto)
      else:
        print(f"No existe la tarjeta con indice {indice_tarjeta}.")
        return self
      
      def pagar_tarjetas(self, monto, indice_tarjeta=0):
         """Realiza un pago en la tarjeta especificada por el indice"""
         if 0<= indice_tarjeta < len(self.tarjetas):
            self.tarjetas[indice_tarjeta].pago(monto)
         else:
            print(f"No existe la tarjeta con el indice {indice_tarjeta}.")
         return self
      
      def mostrar_saldo_usuario(self):
         """Muestra el saldo de todas las tarjetas del usuario"""
         print(f"Saldo de las tarjetas del usuario{self.nombre}:")
         for i, tarjeta in enumerate (self.tarjetas, 1):
            print(f"Tarjeta {i}: Saldo a pagar: ${tarjeta.saldo_pagar}:,")
            return self 
         

         
