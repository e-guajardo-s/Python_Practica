dinero = float(input("Ingrese el dinero a invertir: "))
interes = float(input("Ingrese el interes anual: "))
años = int(input("Ingrese los años a invertir"))

#Un numero float o flotante es aquel que tiene decimales

capital = round(dinero * ((interes/100)+1)**años,2)

#round o redondear sirve para redondear un numero segun los decimales deseados
#En este caso redondie 2 decimales (0,00) pero se puede redondear n veces siguiendo la formula
#round(n1, n2) donde n1 es el numero flotante y n2 el nro de decimales a mostrar despues de la

print(f"Su capital sera: {capital}")