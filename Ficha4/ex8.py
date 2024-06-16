#Função area() que recebe largura e comprimento e retorna a área do terreno

def area(largura, comprimento):
    return largura * comprimento

def numero_positivo(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            if numero > 0:
                return numero
            else:
                print("O valor tem ser um número positivo.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")

# Solicitar ao usuário a largura e o comprimento do terreno, verificando se são válidos
largura = numero_positivo("Diga a largura do terreno: ")
comprimento = numero_positivo("Diga o comprimento do terreno: ")

# Calcular a área do terreno
resultado_area = area(largura, comprimento)

# Exibir o resultado
print(f"A área do terreno com largura {largura} e comprimento {comprimento} é: {resultado_area}")