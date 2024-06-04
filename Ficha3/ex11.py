#Pedir um numero e indicar a tabuada de 1 a 10 
numero = int(input("Indique um numero: "))

# Exibir a tabuada de 1 a 10

print(f"Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

