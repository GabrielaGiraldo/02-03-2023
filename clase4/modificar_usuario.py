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