# Pedir 2 numeros e a operação e apresentar o resultado

numero1 = int(input("Indica um numero:"))
numero2 = int(input("Indica um numero:"))
operacao = str(input("Indica a operação a realizar:")).lower()

if operacao == "multiplicação":
    print (f"{numero1}*{numero2}={numero1*numero2}")
elif operacao == "subtração":
    print (f"{numero1}-{numero2}={numero1-numero2}")
elif operacao == "divisão" :
    print (f"{numero1}/{numero2}={numero1/numero2}")
elif operacao == "adição":
    print (f"{numero1}+{numero2}={numero1+numero2}")
