# Pedir um número ao utilizador
numero = int(input("Indique um número: "))

# Calcular a soma dos números pares de 1 até o número fornecido
soma_pares = 0
for i in range(1, numero + 1):
    if i % 2 == 0:
        soma_pares += i

# Exibir o resultado
print(f"A soma dos números pares de 1 até {numero} é: {soma_pares}")