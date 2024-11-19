# Solicita un número al usuario y almacena en una lista los resultados de su tabla de multiplicar
# hasta el 10. Por ejemplo, si el número es 5, la lista contendrá: 5,10,15,20,25,30,35,40,45,50

while True:
    try:
        numero = int(input("Ingresa un número: "))
        if numero <= 0:
            raise ValueError("El número debe ser mayor que cero.")
        break
    except ValueError as e:
        print(f"Entrada no válida: {e}. Por favor, ingresa un número entero positivo.")

tabla = [numero * i for i in range(1, 11)]

print(f"Tabla de multiplicar del {numero}:", tabla)

tabla_detallada = [(numero, i, numero * i) for i in range(1, 11)]

print("\nMultiplicando | Multiplicador | Resultado")
print("----------------------------------------")

for multiplicando, multiplicador, resultado in tabla_detallada:
    print(f"{multiplicando:^12} | {multiplicador:^13} | {resultado:^9}")
