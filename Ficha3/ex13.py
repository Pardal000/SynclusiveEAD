#Calcular a soma dos numeros pares desde 1 até ao pedido
numero = int(input("Indique um numero: "))

soma = 0

for i in range(1, numero):
    if i % 2 == 0:
        soma += i 

print(f"A soma desde 1 até {numero} é : {soma}")
