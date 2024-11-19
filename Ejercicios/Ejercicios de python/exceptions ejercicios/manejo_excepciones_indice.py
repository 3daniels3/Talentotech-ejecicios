# Localiza el error en el siguiente bloque de código. Crea una excepción para evitar
# que el programa se bloquee y explica en un mensaje al usuario la causa y/o solución:
# lista = [1, 2, 3, 4, 5] 
# print(lista[10])


lista = [1, 2, 3, 4, 5]

try:
    print(lista[10])
except IndexError:
    print("Error: Indice fuera de rango.")
    print("Revisa el índice. Los índices disponibles son desde 0 hasta", len(lista)-1)
