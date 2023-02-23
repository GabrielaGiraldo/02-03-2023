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