class Cuenta():
    
    def __init__(self,titular,cantidad=0):
        self.titular = titular
        self.cantidad = cantidad
    
    def ver(self):
        #x = input("¿Desea ver su saldo?(si/no)")
        #if x == "si":
        print(f"{self.titular} su saldo actual es {self.cantidad}")
    def ingresar(self):
        ingre = float(input("¿Cuánto deseas ingresar?"))
        if ingre > 0:
            self.cantidad = self.cantidad + ingre
    def retirar(self):
        reti = float(input("¿Cuánto desea retirar?"))
        self.cantidad = self.cantidad - reti
        if self.cantidad < 0:
            print(f"{self.titular} tiene {self.cantidad} de deuda")

titular = Cuenta ("Gabriela")
titular.ingresar()
titular.retirar()
titular.ver()
print(titular)