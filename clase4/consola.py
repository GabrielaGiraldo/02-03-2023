from funciones import *
from modificar_usuario import mod_usuario
def consola(prestamo):
    
    while True:
        print(
            """_
        1.Ingresar usuario
        2.Eliminar usuario
        3.Actualizar usuario
        4.Visualizar usuario
        (x). Salir
    """
        )
        eleccion = input("Que desea hacer:")
        match eleccion:
            case "1":
                print(agregar_usuario(prestamo))
            case "2":
                print(eliminar_usuario(prestamo))
            case "3":
                print(mod_usuario(prestamo))
            case "4":
                print(visualizar_usuario(prestamo))
            case "x":
                print("El programa finalizo")
                break
            
        