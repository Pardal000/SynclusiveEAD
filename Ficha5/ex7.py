#Classe Elevador atributos como andar_atual capacidade_atual, andar_limite e capacidade_limite
#Elevador começa sempre no res de chao (andar 0) e não há subterraneos Metodos subir() descer() entra() sai()


class Elevador:
    def __init__(self,capacidade_atual,andar_limite,capacidade_limite):
        self.capacidade_atual = capacidade_atual
        self.andar_limite = andar_limite
        self.capacidade_limite = capacidade_limite

    @staticmethod
    def obter_andar():
        while True:
            try:
                andar = int(input("Digite o andar para onde quer ir: "))
                return andar
            except ValueError:
                print("Entrada inválida! Por favor, insira um número válido.")


    def subir(self, andar):
        if andar > 0 and andar <= self.andar_limite:
            print(f"O elevador vai subir {andar} andares")
        else:
            print(f"O elevador não pode subir {andar} andares. Limite de andares é {self.andar_limite}.")
    
    def descer(self,andar):
        if andar < 0 and andar <= self.andar_limite:
            print(f"O elevador vai descer {andar} andares")
        else:
            print(f"O elevador não pode descer {andar} andares. Limite de andares é {self.andar_limite}.")

    def sair(self, excesso_pessoas):
        excesso_pessoas = self.capacidade_limite - self.capacidade_atual
        excesso_pessoas_positivo = abs(excesso_pessoas)
        if excesso_pessoas < 0:
            print(f"{excesso_pessoas_positivo} vão ter de sair!")
    
    def entrar(self, excesso_pessoas):
        if excesso_pessoas > 0:
            print(f"Podem seguir!")

    def exibir_informacoes(self):
        print(f"Capacidade atual: {self.capacidade_atual}")
        print(f"Andar limite:{self.andar_limite} ")
        print(f"Capacidade limite:{self.capacidade_limite} ")


# Solicitar ao usuário a capacidade atual do elevador
while True:
    try:
        capacidade_atual = int(input("Digite o numero de pessoas que entrou: "))
        if capacidade_atual >= 0:
            break
        else:
            print("A capacidade atual deve ser um valor não negativo.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido.")


elevador1 = Elevador(capacidade_atual,13,25)

elevador1.exibir_informacoes()

pessoas_entrar = elevador1.pessoas_entrar()
elevador1.entrar(pessoas_entrar)

andares_subir = elevador1.obter_andar()
elevador1.subir(andares_subir)

andares_descer = elevador1.obter_andar()
elevador1.descer(andares_descer)

pessoas_sair = elevador1.pessoas_entrar()
elevador1.sair(pessoas_sair)

elevador1.exibir_informacoes()