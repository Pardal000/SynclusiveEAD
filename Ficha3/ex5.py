#Pede a idade ao utilizador
idade = int(input("Qual é a sua idade:"))

#Fazer if com mais e menos de 12 anos (-12/5-euros, 12/18-7euros, +18-10 euros)

if 0<idade>12 :
    print("O bilhete custa 5 euros")
elif 12<=idade<18 :
    print("O bilhete custa 7 euros")
elif idade>18: 
    print("O bilhete custa 10 euros")
else :
    print("Numero inválido")
