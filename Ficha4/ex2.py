#Procedimento desenhar_retangulo que recebe a largura e altura e imprime um retangulo com essas dimensoes
def desenhar_retangulo(largura, altura):
    for i in range(altura):
        print('-' * largura)

# Solicitar ao usuário a largura e a altura
largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

# Desenhar o retângulo
desenhar_retangulo(largura, altura)