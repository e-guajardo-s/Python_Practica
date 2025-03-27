horas = int(input("Ingrese sus horas trabajadas: "))
# Como ya sabemos input es la entrada de texto en el terminal
# int es para especificar que lo que hay dentro del parentesis es una variable tipo entero (numero)
# esto se aplica para poder hacer las posteriores operaciones que estan en el codigo
choras = int(input("Ingrese el coste por horas: "))

trabajo = horas * choras
# En esta variable se esta multiplicando las "Horas" por el "Coste de las Horas"
# "*" es multiplicacion
print(f"Tu paga es: {trabajo}")
# El resultado de la operacion es la variable trabajo y la mostramos en pantalla