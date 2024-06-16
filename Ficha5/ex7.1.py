class Elevador:
    def __init__(self, capacidade_atual, andar_limite, capacidade_limite):
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

    @staticmethod
    def pessoas_entrar():
        while True:
            try:
                pessoas = int(input("Digite o número de pessoas que entraram: "))
                if pessoas >= 0:
                    return pessoas
                else:
                    print("O número de pessoas deve ser um valor não negativo.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número válido.")

    def subir(self, andar):
        if 0 < andar <= self.andar_limite:
            print(f"O elevador vai subir {andar} andares.")
        else:
            print(f"O elevador não pode subir {andar} andares. Limite de andares é {self.andar_limite}.")

    def descer(self, andar):
        if 0 < andar <= self.andar_limite:
            print(f"O elevador vai descer {andar} andares.")
        else:
            print(f"O elevador não pode descer {andar} andares. Limite de andares é {self.andar_limite}.")

    def sair(self, pessoas):
        if self.capacidade_atual - pessoas >= 0:
            self.capacidade_atual -= pessoas
            print(f"{pessoas} pessoas saíram. Capacidade atual: {self.capacidade_atual}.")
        else:
            print("Não há tantas pessoas no elevador para sair.")

    def entrar(self, pessoas):
        if self.capacidade_atual + pessoas <= self.capacidade_limite:
            self.capacidade_atual += pessoas
            print(f"{pessoas} pessoas entraram. Capacidade atual: {self.capacidade_atual}.")
        else:
            print(f"O elevador não pode acomodar {pessoas} pessoas. Capacidade limite é {self.capacidade_limite}.")

    def exibir_informacoes(self):
        print(f"Capacidade atual: {self.capacidade_atual}")
        print(f"Andar limite: {self.andar_limite}")
        print(f"Capacidade limite: {self.capacidade_limite}")

# Solicitar ao usuário a capacidade atual do elevador
while True:
    try:
        capacidade_atual = int(input("Digite a capacidade atual do elevador: "))
        if capacidade_atual >= 0:
            break
        else:
            print("A capacidade atual deve ser um valor não negativo.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número válido.")

# Criando uma instância da classe Elevador com capacidade atual fornecida pelo usuário
elevador1 = Elevador(capacidade_atual, 13, 25)

# Exibindo as informações do elevador
elevador1.exibir_informacoes()

# Entrar pessoas no elevador
pessoas_entrar = Elevador.pessoas_entrar()
elevador1.entrar(pessoas_entrar)

# Subir andares
andares_subir = Elevador.obter_andar()
elevador1.subir(andares_subir)

# Descer andares
andares_descer = Elevador.obter_andar()
elevador1.descer(andares_descer)

# Sair pessoas do elevador
pessoas_sair = Elevador.pessoas_entrar()
elevador1.sair(pessoas_sair)

# Exibindo novamente as informações do elevador
elevador1.exibir_informacoes()