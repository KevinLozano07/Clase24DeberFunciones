#Deber: Crea una nueva variable global y modifícala dentro de una función.

y = 10

def modificar_global():
 global y
 y = 20
 print(f"Variable global y modificada dentro de la función: {y}")

print("")
modificar_global()
print(f"Variable global y fuera de la función: {y}")
print("")

x = 1

def Mod_global():
 global x
 x = 395
 print(f"La nueva variable global modificada es: {x}")

Mod_global()
print("")