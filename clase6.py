class Coche():
    def __init__(self,matricula,marca,kilometros,gasolina):
        self.matricula = matricula
        self.marca = marca
        self.kilometros = kilometros
        self.gasolina = gasolina
    def avanzar(self,km):
        self.gasolina = self.gasolina - km
        self.kilometros = self.kilometros + km
        if self.gasolina <= 0:
            print(f"El carro se quedo sin gasolina")

gabriela = Coche("HBO133","Chevrolet",45,20)
gabriela.avanzar(15)
print(gabriela.gasolina)
print(gabriela.kilometros)