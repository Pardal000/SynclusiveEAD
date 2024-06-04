# Gerar numero aleatório de 1 a 20 e pedir para adivinhar dando dicas se o palpite foi muito alto ou muito baixo

import random

numero_aleatorio = random.randint(1, 20)

palpite = int(input("Indique um numero: "))

while palpite!=numero_aleatorio:
    if palpite<numero_aleatorio:
        print("O seu numero é muito baixo")
    elif palpite>numero_aleatorio:
        print("O seu numero é muito alto")

    palpite = int(input("Indique outro numero:"))
else:
    print("Certo!!")
