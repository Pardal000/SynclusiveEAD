numero_aluno = int(input("Quantos alunos estão na turma?"))

nome_dos_alunos = []  #criação de uma lista

for i in range(numero_aluno):
    nome = input("Digite o nome do aluno {i+1} :")
    nome_dos_alunos.append(nome)

#append é um método que atribui um valor ao ultimo nome da lista

print("O nome dos alunos são:")
for nome in nome_dos_alunos:
    print(nome)

#Mostra os nomes inseridos na lista 