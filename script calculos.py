import operaciones

# Ejemplo de uso de las funciones del módulo
a = input("Ingrese el primer número: ")
b = input("Ingrese el segundo número: ")

# Suma
resultado_suma = operaciones.suma(a, b)
if resultado_suma is not None:
    print("Resultado de la suma:", resultado_suma)

# Resta
resultado_resta = operaciones.resta(a, b)
if resultado_resta is not None:
    print("Resultado de la resta:", resultado_resta)

# Producto
resultado_producto = operaciones.producto(a, b)
if resultado_producto is not None:
    print("Resultado del producto:", resultado_producto)

# División
resultado_division = operaciones.division(a, b)
if resultado_division is not None:
    print("Resultado de la división:", resultado_division)
