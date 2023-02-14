#def funcion_ejemplo(a,b,c=5):
    # En los parametros de la función a "c" se le asigna un valor "fijo" o "predeterminado" (pre)
    # Los parametros pre no pueden estar ubicados al inicio [def blabla(c=6,a,b):] <- eso estaría mal aplicado
    #lógica
    #d = int(input("Ingrese un numero:"))
    # si se pide una variable dentro de la misma función no se tiene porque pasar por parametros.
    #suma = a + b + d
    #return
    #return suma
#print(funcion_ejemplo(2,3))


lista_estudiante = ["David","Omar","Isaac"]
lista_profe = ["Felipe"]
def agregar(
    lista:list
    
    ) -> list:
    estudiante = input("Añadir:")
    lista.append(estudiante)
agregar(lista_estudiante)
agregar(lista_profe)

def eliminar(
    lista:list
    
    ) -> list:
    estudiante = str(input("Ingresar persona a eliminar:"))
    lista.remove(estudiante)
eliminar(lista_estudiante)
eliminar(lista_profe)
def ver(
    lista:list
    ) -> list:
    x = str(input("Desea ver los usuarios (si/no):"))
    if x == "si":
        print(lista)
ver(lista_estudiante)
ver(lista_profe)