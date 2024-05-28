import random 

#Escolhe um numero aleatorio
numero_aleatorio = random.randint(1,10)

#Nova varaivel para guardar o palpite  
palpite = None


while palpite != numero_aleatorio:

#Pedir o palpite
    palpite = int(input("Adivinhe o numero entre 1 e 10:"))

#Verifica se está correto
    if palpite < numero_aleatorio:
        print("O n é maior")
    elif palpite > numero_aleatorio:
        print ("O n  é menor")
    else:
        print ("Advinhou!!!!")
