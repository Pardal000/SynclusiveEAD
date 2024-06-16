# Classe Telemovel Atributos Marca, Modelo, Capacidade de aramzenamento e armazenamento utilizado Metodo que calcula a capacidade disponivel

class Telemovel:
    def __init__(self,marca,modelo,capacidade_armazenamento,armazenamento_utilizado):
        self.marca = marca
        self.modelo = modelo
        self.capacidade_armazenamento = capacidade_armazenamento
        self.armazenamento_utilizado = armazenamento_utilizado

    def capacidade_disponivel(self):
       return self.capacidade_armazenamento-self.armazenamento_utilizado
    

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Capacidade de Armazenamento: {self.capacidade_armazenamento} GB")
        print(f"Armazenamento Utilizado: {self.armazenamento_utilizado} GB")
        print(f"Capacidade Disponível: {self.capacidade_disponivel()} GB")



telemovel1 = Telemovel("Samsung", "Galaxy S21", 128, 64)

telemovel1.exibir_informacoes()