import random

opcoes =["pedra","papel","tesoura"]

escolha_computador = random.choice(opcoes)

escolha_jogador = input("Escolha pedra, papel ou tesoura:").lower()

print("O Computador escolheu:" ,escolha_computador)

if escolha_computador == escolha_jogador:
    print("Deu empate")
elif (escolha_jogador == "pedra" and escolha_computador =="tesoura") or\
     (escolha_jogador == "papel" and escolha_computador =="pedra" )or\
     (escolha_jogador == "tesoura" and escolha_computador == "pedra"):
    print("Você perdeu!! :(")
else:
    print("Você ganhou!!!")