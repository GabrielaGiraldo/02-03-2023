#lista = []
#def agregar(
#    lista:list
#)->list:
#    x = int(input("Cuántas palabras desea añadir?"))
#    for i in range(x):
#        y = input(f"Ingrese la palabra número {i+1}:")
#        y = y.lower()
#        lista.append(y)
#    print(lista)

#    z = int(input("Cuántas palabras quiere eliminar?"))
#    for j in range(z):
#        d = input(f"Ingrese la palabra número {j+1}:")
#        d = d.lower()
#        lista.remove(d)
#    print(lista)    
#agregar(lista)

def operacion_lista(
    
):
    numerito=int(input("Dijite el numero de palabras que desea añadir a su lista:"))
    lista=[]
    for i in range(numerito):
        d = input(f"Ingrese la palabra número {i+1}:")
        d=d.lower()
        lista.append(d)
    numerito2=int(input("Dijite el numero de palabras que desea añadir a su lista:"))
    lista2=[]
    for j in range(numerito2):
        d = input(f"Ingrese la palabra número {i+1}:")
        d=d.lower()
        lista.append(d)
    for k in lista:
        if k in lista:
            lista.remove(k)
    print("Lista final:",lista)        

