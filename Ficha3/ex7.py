# Pedir três números ao utilizador e armazená-los em uma lista
numeros = []
for x in range(1, 4):
    numero = int(input(f"Digite o {x}º número ({x}/3): "))
    numeros.append(numero)

# Determinar o maior número usando a função max()
maior_numero = max(numeros)

# Exibir o maior número
print(f"O maior número entre os três é: {maior_numero}")