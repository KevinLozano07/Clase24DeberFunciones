#Deber: Modifica el código para que la función interior reciba un parámetro y lo imprima.

def funcionexterior():
  def funcioninterior():
     print("Esta es la función interior")

  funcioninterior()
  print("Esta es la función exterior")

print("")
funcionexterior()
print("")

def funcionext():
 def funcionint():
      x = 10
      print("")
      print(f"La funcion interna contiene el numero: {x}")
      print("")

 funcionint()
 print("Esta es la funcion externa (No posee un valor)")

funcionext()
print("")
