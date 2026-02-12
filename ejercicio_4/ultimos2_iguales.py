# Programa para verificar si los dos ultimos digitos son iguales

# input
print("--------------------------------------")
print("-----------Ultimos digitos guales-------------")
print("--------------------------------------")
s = int(input("digite el número: "))

# Procesing
ultimo_digito = s % 10
penultimo_digito =(s//10)%10
if (ultimo_digito == penultimo_digito):
    rta= "IGUALES"
else:
    rta= "DIFERENTES"

# Output
print("--------------------------------------")
print("-----------RESULTADO---------")
print("--------------------------------------")
print("El número ingresado fue fue: " + str(s))
print("Su ultimo digito es " + str(ultimo_digito))
print("Su penultimo digito es " + str(penultimo_digito))
print("Los dos ultimos digitos son " + rta)
