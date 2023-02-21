def mod_usuario(
    diccionario:dict
)-> dict:
    x = input("¿Desea modificar algun usuario? (si/no): ")
    y = x.lower()
    if y == "si":
        nom = input("Nombre del usuario:")
        n = nom.lower()
        lib = input("Nombre del libro:")
        fecha = input("Fecha de prestamo:")
        dicc_int = {
            
            "libro":lib,
            "fecha":fecha
            
        }
        diccionario[n].append(dicc_int)
    