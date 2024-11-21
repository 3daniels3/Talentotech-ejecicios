# Crear un programa que almacene en una variable un diccionario
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por
# una moneda y muestre su símbolo o un mensaje de error si la moneda
# no está en el diccionario.

simbolos_monedas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
while True:
    moneda = input('\nEscribe el nombre de una moneda: ').capitalize()
    if moneda in simbolos_monedas:
        print(simbolos_monedas[moneda])
        break
    else:
        print('Moneda no encontrada.')
