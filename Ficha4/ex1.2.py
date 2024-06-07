# Imprimir um procedimento com o numero de linhas pedido com o numero em cada linha
def linhas(n_linhas):
    cont=1
    while cont <= n_linhas:
        print ("Linha",cont)
        cont+=1

#Pedir numero de linhas
while True:
        try:
            escolha_linhas = int(input("Numero de linhas"))
            if escolha_linhas > 0:
                break
            else:
                print("O numero tem de ser positivo:")
        except ValueError:
            print ("Entrada inválida!! Indique um numero inteiro!!!") 

linhas(escolha_linhas)