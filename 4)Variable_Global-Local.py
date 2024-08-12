#Deber: Intenta usar la variable global

x = 10 # Variable global

def mi_funcion():
 
 print(f"Variable local x dentro de la función: {x}")

print("")
mi_funcion()
print("")
print(f"Variable global x fuera de la función: {x}")
print("")