def IMC(peso, altura):
    return peso / altura ** 2

peso = float(input("Digita o peso:"))
altura = float(input("DIgita a tua altura:"))

imc = IMC(peso, altura)

print(imc)
