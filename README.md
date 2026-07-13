# Sistema de Registro de Calificaciones

## Descripción del proyecto

Sistema simple en Python para registrar calificaciones de estudiantes, calcular su promedio, determinar si están aprobados o reprobados, y generar un reporte general. Los registros se almacenan en un archivo de texto plano (`notas.txt`).

Este proyecto fue desarrollado como práctica de **Código Limpio** y **Refactorización**, aplicando mejoras incrementales sobre una versión inicial funcional pero con oportunidades de mejora en organización, legibilidad y mantenibilidad. El comportamiento del sistema se mantuvo exactamente igual durante todo el proceso; únicamente se mejoró la calidad interna del código.

## Funcionalidades

- Registrar la calificación de un estudiante (tres notas, cálculo de promedio y estado).
- Listar todos los registros almacenados.
- Generar un reporte con el total de aprobados y reprobados.

## Tecnologías

- Python 3
- Módulo estándar `os`
- Control de versiones con Git y GitHub

## Proceso de refactorización

Se identificaron algunas oportunidades de mejora sobre la versión inicial del código, cada una aplicada y confirmada mediante un commit independiente:

| # | Mejora aplicada | Beneficio |
|---|------------------|-----------|
| 1 | Renombrar funciones y variables con nombres significativos (`p` → `registrar_calificacion`, `n` → `nombre`, etc.) | Código autoexplicativo, más fácil de leer sin necesidad de comentarios |
| 2 | Dividir la función que hacía todo (validar, calcular, determinar estado, guardar) en funciones pequeñas con una sola responsabilidad | Funciones más fáciles de entender, probar y reutilizar |
| 3 | Extraer la lógica repetida de lectura y parseo del archivo en una función reutilizable | Elimina duplicación (principio DRY), un solo punto de cambio |
| 4 | Uso de `with open(...) as archivo:` en lugar de apertura y cierre manual | Manejo seguro de archivos, alineado con las convenciones estándar de Python |
| 5 | Reemplazo de índices numéricos "mágicos" por variables descriptivas al leer cada registro | Mayor claridad sobre qué representa cada dato |

> **Nota:** Ninguna de estas mejoras modificó la funcionalidad del sistema. El objetivo de la refactorización es mejorar la *forma* del código, no su *comportamiento*.

## Cómo ejecutar el proyecto

```bash
python main.py
```

Al ejecutarlo se registran algunos estudiantes de ejemplo, se listan los registros guardados y se muestra el reporte de aprobados/reprobados.

## Historial de commits

El historial de Git refleja el proceso de refactorización paso a paso:

1. `UPDATE: renombrar funciones y variables con nombres descriptivos`
2. `UPDATE: dividir registro de calificaciones en funciones de responsabilidad única`
3. `UPDATE: extraer lectura de registros a función reutilizable para eliminar duplicación`
4. `UPDATE: usar context manager 'with' para el manejo seguro de archivos`
5. `UPDATE: reemplazar índices mágicos por acceso legible a los campos de datos`

## Autor

Proyecto desarrollado por Samara Puga, como parte de la asignatura de Sistemas Ágiles.