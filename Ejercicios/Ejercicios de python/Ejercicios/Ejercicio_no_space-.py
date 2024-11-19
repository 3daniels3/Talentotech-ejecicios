# Pide una cadena por teclado, mete los caracteres en una lista sin espacios.

texto = input("Introduce una cadena de texto: ")

if not texto:
    print("Error: La cadena no puede estar vacía.")
else:
    if texto.isspace():
        print("Error: La cadena no puede contener solo espacios.")
    else:
        caracteres_sin_espacios = [caracter for caracter in texto if caracter != ' ']
        print("\nLista de caracteres sin espacios:", caracteres_sin_espacios)
