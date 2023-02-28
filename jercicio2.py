class Alumno():
    
    def __init__(self,nom):
        self.nom = nom
    def aprobo(self):
        nota = float(input("Ingrese su nota:"))
        if nota >= 6 and nota <= 10:
            print(f"{self.nom} aprobó")
        if nota <= 5 and nota >= 1:
            print(f"{self.nom} reprobó")

estu = Alumno("Gabriela")
estu.aprobo()
print(estu)        