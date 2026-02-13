#precio de reventa

import time
print("-----------------------------------------------------------")
print("Programa para calcular el precio de venta para una tienda")
print("-----------------------------------------------------------")

#input
P_C = int(input("Digite el precio de su producto: "))

#proceso
if P_C <= 3000:
    n = P_C * 0.15
    P_V = P_C + n
else:
    if P_C > 6000:
        n = P_C * 0.25
        P_V= P_C + n
    else:
        P_V = P_C + 500

#output
print("-----------------------")
print("------RESULTADO--------")
print("-----------------------")
print("el nuevo precio es: " + str(P_V))