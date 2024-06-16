#Classe Circulo Atributo Raio Metodos que calculam a área e o perimetro 
import math


class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def obter_raio():
        while True:
            try:
                raio = float(input("Digite o valor do raio do círculo: "))
                if raio > 0:
                    return raio
                else:
                    print("O valor do raio deve ser um número positivo.")
            except ValueError:
                print("Entrada inválida! Por favor, insira um número válido.")

    def area(self):
        return math.pi * self.raio**2
    
    def perimetro(self):
        return 2 * math.pi * self.raio
    
    def exibir_informacoes(self):
        area = self.area()
        perimetro = self.perimetro()
        print(f"Raio: {self.raio}")
        print(f"Área: {area:.2f}")
        print(f"Perímetro: {perimetro:.2f}")

raio = Circulo.obter_raio()

circulo1 = Circulo(raio)

circulo1.exibir_informacoes()