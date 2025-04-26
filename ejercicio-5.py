#Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

Cuentatotal = int(input("Digita el total de la cuenta: "))
print("lLos porcentajes de la propina son: 10%, 15%, 20%" )
Porcentajes= int(input("Digita que quieres darnos: "))
Propina=Cuentatotal*(Porcentajes/100)
print(Propina)

