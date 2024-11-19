# Crea una función llamada agregar_una_vez(lista, el) que reciba una lista
# y un elemento. La función debe añadir el elemento al final de la lista, 
# siempre y cuando no sea un duplicado. Si el elemento ya está en la lista, 
# se debe generar una excepción de tipo ValueError y mostrar este mensaje:
# Error: No se pueden agregar elementos duplicados => [elemento].

def agregar_una_vez(lista, elemento):
    try:
        if elemento in lista:
            raise ValueError(
                f"\nError: No se pueden agregar elementos duplicados => [{elemento}]")
        else:
            lista.append(elemento)
    except ValueError as e:
        print(e)


mi_lista = [0, 1, 2, 3, 4, 5, 6, 7]
agregar_una_vez(mi_lista, 4)
agregar_una_vez(mi_lista, 8)
print(mi_lista)
