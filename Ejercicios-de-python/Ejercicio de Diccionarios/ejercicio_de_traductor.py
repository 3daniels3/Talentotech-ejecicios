# Crear un programa que construya un diccionario de traducción de español a inglés.
# El usuario ingresará las palabras en español e inglés, separadas por dos puntos,
# y cada par <palabra>:<traducción> estará separado por comas. El programa debe formar un
# diccionario con las palabras y sus traducciones. Luego pedirá una frase en español
# y utilizará el diccionario para traducirla palabra por palabra. Si una palabra no se encuentra
# en el diccionario, se dejará sin traducir.

def generar_diccionario(traducciones):
    diccionario_traduccion = {}

    elementos = traducciones.split(",")
    for elemento in elementos:
        palabra, traduccion = elemento.split(":")
        diccionario_traduccion[palabra.strip()] = traduccion.strip()

    return diccionario_traduccion


def traducir_texto(texto, diccionario):
    palabras = texto.split()
    texto_traducido = []
    for palabra in palabras:
        if palabra in diccionario:
            texto_traducido.append(diccionario[palabra])
        else:
            texto_traducido.append(palabra)

    return " ".join(texto_traducido)


entradas_traduccion = input(
    "Introduce las palabras en el formato <palabra>:<traducción>, separadas por comas: ")
diccionario_traducido = generar_diccionario(entradas_traduccion)

texto_a_traducir = input("Introduce una frase en español para traducir: ")

texto_traducido = traducir_texto(texto_a_traducir, diccionario_traducido)
print("Texto traducido:", texto_traducido)
