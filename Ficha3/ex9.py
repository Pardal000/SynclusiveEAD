computador = "Pedra"

jogador = str(input("Indica uma jogada (Pedra,Papel,Tesoura):"))

if jogador == "Pedra":
    print("Deu Empate!!")
elif jogador == "Papel":
    print("Ganhou!!")
elif jogador == "Tesoura":
    print("Perdeu!!")
else:
    print("Inválido!")