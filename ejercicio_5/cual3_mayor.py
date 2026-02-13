# calcular cual es el mayor de los tres

# input
print("--------------------------------------")
n1 = float(input("digite el primer digito: "))
print("--------------------------------------")

print("--------------------------------------")
n2 = float(input("digite el segundo digito: "))
print("--------------------------------------")

print("--------------------------------------")
n3 = float(input("digite el tercer digito: "))
print("--------------------------------------")

# Procesing
if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

# Output
print("--------------------------------------")
print("-----------RESULTADO---------")
print("--------------------------------------")
print("El número mayor es: "+str(mayor))
print("--------------------------------------")