#Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

Numeroano = int(input("Digita un año: "))

if Numeroano % 4 != 0: 
    print ("El año no es bisiesto")
elif Numeroano % 4 == 0: 
    print ("El año si es bisiesto")
elif Numeroano % 100 == 0: 
        print ("El año si es bisiesto")
elif Numeroano % 400 == 0: 
        print ("El año si es bisiesto")
               

