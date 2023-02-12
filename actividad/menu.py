import añadir
import eliminar
import cambiar
import ver
def menu(y):
    condicion = True
    while condicion:
        print(
        """_
        1.Ingresar usuario
        2.Actualizar usuario
        3.Eliminar usuario
        4.Visualizar usuario
        (x). Salir
    
    """
    )
        selec = str(input("Que desea visualizar: "))
        
        if selec == "1":
            print(añadir(y))
        if selec == "2":
            print(eliminar(y))
        if selec == "3":
            print(cambiar(y))
        if selec == "4":
            print(ver(y))
        if selec == "x":
            print("salio de la biblioteca")
            break
