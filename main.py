import os

ARCHIVO = "notas.txt"

def validar_datos(nombre, nota1, nota2, nota3):
    return nombre != "" and nota1 >= 0 and nota2 >= 0 and nota3 >= 0

def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def determinar_estado(promedio):
    return "APROBADO" if promedio >= 7 else "REPROBADO"

def guardar_registro(nombre, nota1, nota2, nota3, promedio, estado):
    with open(ARCHIVO, "a") as archivo:
        archivo.write(
            f"{nombre},{nota1},{nota2},{nota3},{promedio},{estado}\n"
        )
    print("Registro guardado")

def registrar_calificacion(nombre, nota1, nota2, nota3):

    if validar_datos(nombre, nota1, nota2, nota3):
        promedio = calcular_promedio(nota1, nota2, nota3)
        estado = determinar_estado(promedio)
        guardar_registro(nombre, nota1, nota2, nota3, promedio, estado)
    else:
        print("Datos incorrectos")

def leer_registros():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as archivo:
        registros = [linea.strip().split(",") for linea in archivo]
    return registros

def listar_registros():

    registros = leer_registros()
    if not registros:
        print("No existen registros")
        return

    print("-" * 70)
    for datos in registros:
        print(
            datos[0],
            datos[1],
            datos[2],
            datos[3],
            datos[4],
            datos[5]
        )

def generar_reporte():

    registros = leer_registros()
    if registros:
        aprobados = 0
        reprobados = 0

        for datos in registros:
            if datos[5] == "APROBADO":
                aprobados += 1
            else:
                reprobados += 1

        print("Aprobados:", aprobados)
        print("Reprobados:", reprobados)

registrar_calificacion("Ana", 8, 9, 10)
registrar_calificacion("Luis", 5, 6, 4)
registrar_calificacion("Carlos", 7, 8, 6)

listar_registros()

generar_reporte()