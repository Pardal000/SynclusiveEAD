#Procedimento desenhar_retangulo que recebe a largura e altura e imprime um retangulo com essas dimensoes
def verificar_dimensoes():
    while True:
        try:
            largura = int(input("Digite a largura do retângulo: "))
            altura = int(input("Digite a altura do retângulo: "))
            if largura > 0 and altura > 0:
                return largura, altura
            else:
                print("A largura e a altura devem ser números inteiros positivos.")
        except ValueError:
            print("Entrada inválida! Por favor, insira números inteiros.")

def desenhar_retangulo(largura, altura):
    for i in range(altura):
        print("-" * largura)

# Solicitar ao usuário a largura e a altura, verificando se são válidos
largura, altura = verificar_dimensoes()

# Desenhar o retângulo
desenhar_retangulo(largura, altura)