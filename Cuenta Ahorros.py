balance_inicial= int(input("Ingrese su balance inicial: "))
balance1 = round(balance_inicial * (1 + 0.04), 2)
balance2 = round(balance1 * (1 + 0.04), 2)
balance3 = round(balance2 * (1 + 0.04), 2)

print(f"El balance final seria de:\n1 año: {balance1}\n2 años: {balance2}\n3 años: {balance3}")