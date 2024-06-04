#Pedir 2 numeros e imprimir todos os numeros inteiros entre um e outro 
numero1 = int(input("Indique o primiero numero: "))
numero2 = int(input("Indique o segundo numero: "))

for x in range (numero1-1,numero2):
    numerario=x+1
    print(f"{numerario}")