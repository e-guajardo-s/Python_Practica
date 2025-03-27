peso =int(input("Ingrese su peso en kg: "))
altura =float(input("Ingrese su  en metros: "))
# Float es para indicar que es lo que esta dentro de la variable es un caracter flotante con comas, osea un numero decimal o entero
# que tiene comas EJ: 1.8, 2.2, 0.5, 24.7
imc= round((peso)/(altura)**2,2)
# round es una funcion para redondear un numero decimal y el ,(numero) es el numero de decimales redondeados, en este caso se redondea
# a dos = round(3.141516,2) = 3.14
print(f"Su indice de masa corporal es: {imc}")