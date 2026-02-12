# Programa para verificar si un número es par

# input
print("--------------------------------------")
print("-----------Número par/impar-------------")
print("--------------------------------------")
XD = int(input("digite el número: "))

# Procesing
mod = XD%2
if (mod == 0):
    rta= "PAR"
else:
    rta= "IMPAR"

# Output
print("--------------------------------------")
print("-----------RESULTADO---------")
print("--------------------------------------")
print("El número " + str(XD) + " es " + rta)