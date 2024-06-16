import math 

class Ponto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

# metodos para alterar x e y 
def set_x (self,x):
    self.x= x

def set_y (self,y):
    self.y = y

#metodos para obter os valores
def get_x(self):
    return self.x

def get_y(self):
    return self.y

#calcular a distancia até a origem
def dist_origem (self):
    return math.sqrt(self.x**2 + self.y**2)

ponto = Ponto (5,4)
print("As coordenadas do nosso ponto são:" ,ponto.get_x(),ponto.get_y())
