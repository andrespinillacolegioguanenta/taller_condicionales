# Programa para verificar si un número es positivo

# input
print("--------------------------------------")
print("-----------Número positivo-------------")
print("--------------------------------------")
x = int(input("digite el número: "))

# Procesing
if (x>=0):
    rta= "POSITIVO"
else:
    rta= "0"
    rta= "NEGATIVO"

# Output
print("--------------------------------------")
print("-----------RESULTADO---------")
print("--------------------------------------")
print("El número " +  " es " + rta)