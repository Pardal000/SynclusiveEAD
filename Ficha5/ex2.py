#Classe Livro Atributos titulo, autor, numero de paginas Metodo para exibir as informações

class Livro:
    def __init__(self,titulo,autor,n_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.n_de_paginas = n_de_paginas

        
    def exibir_informações(self):
        print(f"O nome do livro é {self.titulo}")
        print(f"O Autor é {self.autor}")
        print(f"O Número de Páginas é {self.n_de_paginas}")

livro1 = Livro("Harry Potter", "JK","380")

livro1.exibir_informações()