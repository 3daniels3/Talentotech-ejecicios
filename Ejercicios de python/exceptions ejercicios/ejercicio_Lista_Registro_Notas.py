# REALIZAR UN PROGRAMA DONDE SE MUESTRE LAS NOTAS DE LOS ESTUDIANTES, DE MATEMATICAS, 
# FISICA Y QUIMICA. EL PROGRAMA DEBE MOSTRAR EN UNA LISTA LAS NOTAS PROMEDIOS DE LAS MATERIAS. 
# SI LA NOTA ES INFERIOR A 3, DEBE MOSTRAR UN MENSAJE DE QUE MATERIA VA PERDIENDO, SI POR ERROR
# EL USUARIO INGRESA UNA NOTA MAYOR DE 5 O NEGATIVA, EVITAR EL ERROR POSIBLE, Y REALICE LA SUBSANACION

def obtener_nota(materia):
    while True:
        try:
            nota = float(input(f"Ingrese la calificación de {materia}: "))
            if nota < 0 or nota > 5:
                print("Error: La calificación debe estar entre 0 y 5. Intenta de nuevo.")
            else:
                return nota
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def verificar_materias_perdidas(notas):
    materias_perdidas = []
    if notas[0] < 3:
        materias_perdidas.append("Matemáticas")
    if notas[1] < 3:
        materias_perdidas.append("Física")
    if notas[2] < 3:
        materias_perdidas.append("Química")
    
    if materias_perdidas:
        print("El estudiante está reprobando las siguientes materias:", ", ".join(materias_perdidas))
    else:
        print("El estudiante ha aprobado todas las materias.")

def mostrar_notas_y_promedio(notas, promedio):
    print("\nCalificaciones de las asignaturas:")
    print(f"Matemáticas: {notas[0]}")
    print(f"Física: {notas[1]}")
    print(f"Química: {notas[2]}")
    print(f"Promedio general: {promedio:.2f}")
    
    verificar_materias_perdidas(notas)

def ejecutar():
    print("Bienvenido al sistema de gestión de calificaciones.")
    
    matematicas = obtener_nota("Matemáticas")
    fisica = obtener_nota("Física")
    quimica = obtener_nota("Química")
    
    notas = [matematicas, fisica, quimica]
    
    promedio = calcular_promedio(notas)
    
    mostrar_notas_y_promedio(notas, promedio)

if __name__ == "__main__":
    ejecutar()
