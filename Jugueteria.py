
#Peso de productos
payaso = 112
muñeca = 75

p_pedido = int(input("Ingrese cantidad de payasos: "))
m_pedido = int(input("Ingrese cantidad de muñecas: "))

p_payaso = payaso * p_pedido
p_muñeca = muñeca * m_pedido

p_total = p_payaso + p_muñeca 
print(f"El peso total es: {str(p_total)}")

detalle = input("Desea el detalle? (S/N): ")

if detalle == "S":
    print(f"El peso de los payasos es de: {str(p_payaso)}\ny el peso muñecas es de: {str(p_muñeca)}")
elif detalle == "N":
    print("Programa finalizado.")
else:
    print("Error.")