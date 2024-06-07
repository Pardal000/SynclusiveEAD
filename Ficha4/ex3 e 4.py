#Procedimento desenhar_triangulo que imprime triangulo equilatero com a altura dada
def verificar_altura():
    while True:
        try:
            altura = int(input("Digite a altura do retângulo: "))
            if altura > 0:
                return altura
            else:
                print("A altura deve ser um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")


def desenhar_triangulo(altura):
    for x in range(0, altura):
        # Calcula o número de espaços e de asteriscos
        espacos = altura - x - 1
        asteriscos = 2 * x + 1
        print(" " * espacos + "*" * asteriscos)

# Solicitar ao usuário a altura, verificando se é válida
altura = verificar_altura()

# Desenhar o triângulo
desenhar_triangulo(altura)