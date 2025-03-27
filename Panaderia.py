precio= 3.49
pan_nofresco = int(input("Ingrese la cantidad de barras de pan no frescas vendidas en el dia: "))
subtotal= pan_nofresco * precio
total = round((subtotal * (1 - 0.6)), 2)
print(f"Total\nItem: Pan\nCantidad: {pan_nofresco}\nSubtotal: {subtotal}€\nDescuentos: 60%\nTotal: {total}€\n")
print(f"\nEl precio habitual del una barra de pan es de {precio}€\nEl descuento de barra de pan no fresca es de un 60%\nEl coste final total seria de: {total}")