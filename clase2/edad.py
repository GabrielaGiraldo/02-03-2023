lista_edades_a=[10,15,14,18,19,20,59]
lista_edades_b=[13,12,19,18,18,17,80]

def mayor_de_edad(
    x:list,
    y:list
)->list:
    suma = x+y
    lista_mayor_edad=[]
    for i in suma:
        if i >= 18:
            lista_mayor_edad.append(i)
            print(len(lista_mayor_edad))
    print(lista_mayor_edad)            
mayor_de_edad(lista_edades_a,lista_edades_b)