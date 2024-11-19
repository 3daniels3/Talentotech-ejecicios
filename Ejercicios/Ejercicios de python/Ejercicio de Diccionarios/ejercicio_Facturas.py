facturas = {}

total_recibido = 0
total_por_cobrar = 0


def mostrar_resumen():
    print(f"\nMonto recibido hasta ahora: {total_recibido}")
    print(f"Monto pendiente por cobrar: {total_por_cobrar}\n")


while True:
    print("Elija una opción:")
    print("1. Añadir factura nueva")
    print("2. Pagar una factura")
    print("3. Finalizar programa")

    opcion = input("Elija opción: ").strip()

    if opcion == "1":
        numero_factura = input("Indique el número de la factura: ").strip()
        if numero_factura in facturas:
            print("Este número de factura ya está registrado.")
            continue

        try:
            coste_factura = float(input("Indique el monto de la factura: ").strip())
            if coste_factura <= 0:
                print("El monto de la factura debe ser un número positivo.")
                continue
        except ValueError:
            print("El monto de la factura debe ser un valor numérico.")
            continue

        facturas[numero_factura] = coste_factura
        total_por_cobrar += coste_factura
        print(f"Factura {numero_factura} añadida con un monto de {coste_factura}.")

    elif opcion == "2":
        if not facturas:
            print("No hay facturas pendientes de pago.")
        else:
            print("Facturas pendientes de pago:")
            for numero, coste in facturas.items():
                print(f"Factura {numero}, Monto: {coste}")

            numero_factura = input("Indique el número de factura a pagar: ").strip()

            if numero_factura in facturas:
                coste_factura = facturas.pop(numero_factura)
                total_recibido += coste_factura
                total_por_cobrar -= coste_factura
                print(f"Factura {numero_factura} pagada con un monto de {coste_factura}.")
            else:
                print("Factura no encontrada.")

    elif opcion == "3":
        print("Finalizando el programa.")
        break

    else:
        print("Opción incorrecta. Intente nuevamente.")

    mostrar_resumen()  