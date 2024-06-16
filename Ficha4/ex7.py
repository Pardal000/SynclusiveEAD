#Função chamada verificar_primo que recebe um parametro e retorna True se for primo e False se for o contrário

def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numero_positivo():
    while True:
        try:
            numero = int(input("Digite um numero positivo:"))
            if numero > 0:
                return numero
            else:
                print("O valor tem ser um número positivo.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")

numero = numero_positivo()

resultado = verificar_primo(numero)

if resultado:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")