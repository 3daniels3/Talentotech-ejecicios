# Realizar la carga de dos números enteros por teclado e imprimir su suma,
# luego preguntar si quiere seguir sumando valores.
while True:
    try:
        numero1 = int(input("Introduce el primer número: "))
        numero2 = int(input("Introduce el segundo número: "))
        resultado = numero1 + numero2
        print("El resultado de la suma es:", resultado)
    except ValueError:
        print("Error: Debes ingresar solo números.")
    
    continuar = input("¿Quieres realizar otra operación? [S/N]: ")
    if continuar.upper() == "N":
        break
