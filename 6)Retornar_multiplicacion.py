#Deber: Añade una tercera operación (multiplicación) a la función y retorna su resultado también.

def operaciones_basicas(a, b):
 suma = a + b
 resta = a - b
 multiplicacion = a * b
 return suma, resta, multiplicacion

resultadosuma, resultado_resta, resultado_multiplicacion = operaciones_basicas(8, 3)

print("")
print(f"Suma: {resultadosuma}, Resta: {resultado_resta}, Multiplicacion: {resultado_multiplicacion}")
print("")