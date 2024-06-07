# Imprimir um procedimento com o numero de linhas pedido com o numero em cada linha
def linhas(n_linhas):
    
    cont=1
    while cont <= n_linhas:
        print ("Linha",cont)
        cont+=1
    print("Sou o contador de linhas!!")
    while True:
        escolha_linhas = int(input("Diga o numero de linhas:"))
        if escolha_linhas>0:
            break
        else:
            print("O numero tem de ser positivo:")

    linhas(escolha_linhas)