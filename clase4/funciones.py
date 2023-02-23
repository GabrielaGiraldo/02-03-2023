def agregar_usuario(
    diccionario:dict
)-> dict:
    x = input("¿Desea agregar un nuevo usuario? (si/no):")
    y = x.lower()
    if y == "si":
        
        nom = input("Ingrese su nombre: ")
        n = nom.lower()
        lib =  input("Ingrese su libro: ")
        estado = input("Estado:")
        fecha_pres =  input("Ingrese fecha de prestamo:")
        diccionario_int = {
            "libro":lib,
            "fecha":fecha_pres,
            "estado": estado
        }
    else: 
        print("No desea añadir ningun usuario")
    if diccionario.get(n) != None:
        diccionario[n].append(diccionario_int)
    else:
        diccionario[n] = [diccionario_int]
    print(diccionario)
    
def eliminar_usuario(
    diccionario:dict
)-> dict:
    x = input("¿Desea eliminar un usuario? (si/no):")
    y = x.lower()
    if y == "si":
        nom = input("Que usuario desea eliminar: ")
        n = nom.lower()
        del diccionario[n]
    else: 
        print("No desea eliminar ningun usuario")
    print(diccionario)

def modificar_usuario(
    diccionario:dict
)-> dict:
    x = input("¿Desea modificar un usuario? (si/no):")
    y = x.lower()
    if y == "si":
        modi = input("¿Que usuario desea modificar?")
        mod = modi.lower()
        diccionario.get(mod)
        lib =  input("Ingrese su libro: ")
        estado = input("Estado:")
        fecha_pres =  input("Ingrese fecha de prestamo:")
        diccionario["libro"] = lib
        diccionario["estado"] = estado
        diccionario["fecha"] = fecha_pres
        print(diccionario) 
    

def visualizar_usuario(
    diccionario:dict
    )-> dict:
    x = input("¿Desea visulizar un usuario? (si/no):")
    y = x.lower()
    if y == "si":
        for i in diccionario.items():
            acc = input("¿Desea visulizar un usuario en especifico? (si/no):")
            if acc == "si":
                mostrar = input("Que usuario desea ver:")
                m = mostrar.lower()
                z = diccionario.get(m)
                print(z)
                break
            else:
                print(diccionario)
                break
                
    