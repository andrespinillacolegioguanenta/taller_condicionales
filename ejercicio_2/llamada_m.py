# Calcular el costo de la llamada

# input
print("--------------------------------------")
print("-----------COSTO LLAMADA-------------")
print("--------------------------------------")
m = int(input("digite la duración de la llamada en minutos: "))

# Procesing
if (m <= 3):
    costo_llamada= 500
else:
    costo_llamada= 500 + (m - 3)*100

# Output
print("--------------------------------------")
print("-----------RESULTADO---------")
print("--------------------------------------")
print("Duración de la llamada: " + str(m) + " minutos")
print("Costo de lamada: " + str(costo_llamada)) 