# Função chamada calcular com 2 n e um operador como parametros e retorna o resultado da operação (operação pode ser +-*/)

def obter_numero(mensagem):
    while True:
        try:
            numero=float(input(mensagem))
            return numero
        except ValueError:
            print("Insira um numero válido")


def obter_operador():
    operadores_validos = {'+', '-', '*', '/'}
    while True:
        operador = str(input("Digite o operador (+ - * /): "))
        if operador in operadores_validos:
            return operador
        else:
            print("Operador inválido!")


def calculo (numero1, numero2, operador):
    if operador == "+":
        return numero1+numero2
    elif operador == "-":
        return numero1-numero2
    elif operador == "*":
        return numero1*numero2
    elif operador == "/":
        if numero2 != 0:
            return numero1/numero2
        else: 
            print("Não é possivel dividir por 0!")
    else:
        print("Operador inválido")


numero1 = obter_numero("Digite o primeiro número: ")
numero2 = obter_numero("Digite o segundo número: ")
operador = obter_operador()

resultado = calculo (numero1, numero2, operador)

print(f"O resultado de {numero1} {operador} {numero2} = {resultado}")