# Função chamada contar_palavras que recebe uma frase e retona o n de palavras na frase
def contar_palavras(frase):
    # Dividir a frase em palavras usando o método split()
    palavras = frase.split()
    # Retornar o número de palavras
    return len(palavras)

def verificar_frase():
    while True:
        frase = input("Digite uma frase: ").strip()
        if frase:
            return frase
        else:
            print("A frase não pode estar vazia. Por favor, insira uma frase válida.")

# Solicitar ao usuário para inserir uma frase, verificando se é válida
frase = verificar_frase()

# Contar o número de palavras na frase
numero_de_palavras = contar_palavras(frase)

# Exibir o número de palavras
print(f"A frase contém {numero_de_palavras} palavras.")