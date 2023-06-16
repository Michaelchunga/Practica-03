3# Ejercicio 1
def obtener_porcentaje_combustible():
    while True:
        try:
            fraccion = input("Ingrese la fracción en el formato X/Y: ")
            numerador, denominador = map(int, fraccion.split('/'))
            if numerador < 0 or denominador <= 0:
                raise ValueError
            if numerador < denominador:
                porcentaje = round(numerador / denominador * 100)
                if porcentaje < 1:
                    return "E"
                elif porcentaje > 99:
                    return "F"
                else:
                    return f"{porcentaje}%"
            else:
                raise ValueError
        except ValueError:
            print("Error: La fracción debe estar en el formato X/Y, donde X e Y son números enteros positivos y X >= Y.")
        except ZeroDivisionError:
            print("Error: El denominador no puede ser cero.")

resultado = obtener_porcentaje_combustible()
print("Cantidad de combustible en el tanque:", resultado)

# Ejercicio 2
def obtener_calificaciones():
    calificaciones = input("Introduce una lista de calificaciones separadas por comas: ")
    calificaciones_lista = calificaciones.split(",")

    calificaciones_enteros = []

    for calificacion in calificaciones_lista:
        try:
            calificacion_entero = int(calificacion.strip())
            calificaciones_enteros.append(calificacion_entero)
        except ValueError:
            print(f"Error: '{calificacion}' no es una calificación válida.")

    return calificaciones_enteros

calificaciones = obtener_calificaciones()
print("Calificaciones convertidas en enteros:", calificaciones)

# Ejercicio 3
def triangle_pascal(n):
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i-1]
        curr_row = [1]
        for j in range(1, i):
            curr_row.append(prev_row[j-1] + prev_row[j])
        curr_row.append(1)
        triangle.append(curr_row)
    
    for row in triangle:
        print(' '.join(str(num) for num in row))

# Ejemplo de uso
n = 5
triangle_pascal(n)

# Ejercicio 4

def longitud_ultima_palabra(cadena):
    # Eliminar espacios al principio y al final de la cadena
    cadena = cadena.strip()

    # Dividir la cadena en palabras usando espacios como separadores
    palabras = cadena.split()

    # Verificar si hay palabras en la cadena
    if palabras:
        # Obtener la última palabra y retornar su longitud
        ultima_palabra = palabras[-1]
        return len(ultima_palabra)
    else:
        # Si no hay palabras, retornar 0
        return 0
cadena = "    el mundo de la globalizacion    "
longitud = longitud_ultima_palabra(cadena)
print(longitud)  

# Ejercicio 5

import script_main

# Generar los números aleatorios
numbers = script_main.generate_random_numbers()

# Mostrar la lista de números generados
script_main.display_numbers(numbers)

# Ordenar y mostrar la lista de números
script_main.sort_numbers(numbers)
