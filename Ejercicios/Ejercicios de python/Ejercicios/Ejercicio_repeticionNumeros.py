# Crea una tupla con números, pide un numero por teclado e indica 
# cuantas veces se repite.

numeros = (12, 5, 83, 75, 57, 19, 4, 5, 3, 25, 3, 3, 7)

while True:
    try:
        numero_a_buscar = int(input("\nIngresa un número para contar cuántas veces aparece: "))
        break
    except ValueError:
        print("Error: Debes introducir un número válido.")

if numero_a_buscar in numeros:
    repeticiones = numeros.count(numero_a_buscar)
    print(f"El número {numero_a_buscar} aparece {repeticiones} veces en la tupla.\n")
else:
    print(f"El número {numero_a_buscar} no está presente en la tupla.\n")
