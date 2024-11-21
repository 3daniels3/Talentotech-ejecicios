#  Crea una tupla con números e indica el numero con mayor valor y el 
#  que menor tenga

numeros = (10, 25, 3, 45, 7, 89, 2, 15)

if numeros:
    if all(isinstance(num, (int, float)) for num in numeros):
        numero_max = max(numeros)
        numero_min = min(numeros)

        print("\nTupla de valores numéricos:", numeros)
        print("\nEl número con el valor más alto:", numero_max)
        print("El número con el valor más bajo:", numero_min, "\n")
    else:
        print("Error: La tupla contiene elementos no numéricos.")
else:
    print("Error: La tupla está vacía.")
