#Pedir numeros
numero1 = int(input("Indique 3 numeros (1/3):"))
numero2 = int(input("Indique 3 numeros (2/3):"))
numero3 = int(input("Indique 3 numeros (3/3):"))

#Print numero maior

if numero1>numero2 and numero1>numero3:
    print(f"O numero maior é o nº {numero1}")
elif numero2>numero1 and numero2>numero3:
    print(f"O numero maior é o nº {numero2}")
elif numero3>numero1 and numero3>numero2:
    print(f"O numero maior é o nº {numero3}")