#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

numero1 = int(input("Digita primer número: "))
numero2 = int(input("DIgita segundo número: "))
print("El primer número es:", numero1)
print("El segundo número es:", numero2)

if numero1 > numero2:
  print("El primer número es mayor que el segundo")
else: 
  print("El primer número es menor que el segundo")
if numero1 == numero2:
    print("El primer número es igual que el segundo")


