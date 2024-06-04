#Pedir um numero e fazer contagem até 0 
numero_pedido = int(input("Indique um numero: "))

for x in range(numero_pedido, -1, -1):
    print(x)

print("Contagem concluída!")