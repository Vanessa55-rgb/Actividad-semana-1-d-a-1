#Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:
#"Bajo peso" si es menor a 18.5
#"Normal" si está entre 18.5 y 24.9
#"Sobrepeso" si está entre 25 y 29.9
#"Obesidad" si es mayor o igual a 30

peso= float(input("Digita su peso en (kg): "))
altura = float(input("Digita su altura en (m): "))

#Fórmula: IMC = peso (kg) / (estatura (m))² 
IMC = peso / altura**2
print("El IMC es:", IMC)

if IMC < 18.5:
  print("Bajo peso")
elif 18.5 <= IMC < 24.9:
  print("Normal")
elif 25 > IMC < 29.9: 
  print("Sobrepeso")
elif IMC >=30:
    print ("Obesidad")

