# Ejrcicio 06

def suma(a, b):
    try:
        resultado = float(a) + float(b)
        return resultado
    except ValueError:
        print("Error: Tipo de dato no válido")

def resta(a, b):
    try:
        resultado = float(a) - float(b)
        return resultado
    except ValueError:
        print("Error: Tipo de dato no válido")

def producto(a, b):
    try:
        resultado = float(a) * float(b)
        return resultado
    except ValueError:
        print("Error: Tipo de dato no válido")

def division(a, b):
    try:
        if float(b) == 0:
            print("Error: No es posible dividir entre cero")
        else:
            resultado = float(a) / float(b)
            return resultado
    except ValueError:
        print("Error: Tipo de dato no válido")


