def cambiar(
    diccionario:dict
) -> dict:
     x = str(input("Desea modificar un usuario? (si/no) "))
     x = x.lower()
     if x == "si":
         ant = str(input("Nombre de usuario por cambiar:"))
         ant = ant.lower()
         nom = str(input("Nombre de usuario: "))
         nom = nom.lower()
         diccionario.pop(ant)
         diccionario.update(nom)
     else:
         print("No se desea cambiar ningun usuario")
print("-"*40)