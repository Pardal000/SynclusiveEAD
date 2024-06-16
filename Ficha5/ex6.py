# Classe Pessoa Atributos nome idade e nacionalidade Metodo que calcula o ano de nascimento recebendo como parametro o ano atual
#Metodo apresentacao() que diz "Olá o meu nome é {nome} e tenho {idade} anos"

class Pessoa:
    def __init__(self,nome,idade,nacionalidade,ano_atual):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade
        self.ano_atual = ano_atual


    def calcular_ano_nascimento(self):
        return self.ano_atual - self.idade


    def apresentacao(self):
        print (f"Olá o meu nome é {self.nome} e tenho {self.idade}")


def obter_ano_atual():
        while True:
            try:
                ano_atual = int(input("Digite o ano atual: "))
                if ano_atual > 2023:
                    return ano_atual
                else:
                    print("O valor do ano atual deve ser mais que 2024.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número válido.")


ano_atual = obter_ano_atual()

pessoa1 = Pessoa("João", 30, "Portuguesa", ano_atual)
pessoa1.apresentacao()

ano_nascimento = pessoa1.calcular_ano_nascimento()
print(f"O meu ano de nascimento é {ano_nascimento}")



        
