#Contagem de 0 até N em que N é um numero dado pelo utilizador
numero = int(input("Indique um numero: "))

for i in range(-1, numero):
    contagem = i + 1
    print(f"Contagem crescente:{contagem}")