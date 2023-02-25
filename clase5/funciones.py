listas = [2,3,4,5]
#Si listas se creara desopues de la función no se podria hacer uso de ella, debe aparecer antes de la función
def funciones(parametros):
    print(parametros)
    listas.append(parametros)
    variable = parametros*2
    listas.append(variable)
    print(listas)
    return parametros
funciones("gabriela")