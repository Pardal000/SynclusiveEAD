#Pedir peso e altura

peso= float(input("Indique o seu peso em Kg:"))
altura= float(input("Indique a sual altura em m:"))

#Fazer indice de massa corporal

IMC_inteiro=peso/(altura**2)
IMC = round(IMC_inteiro, 3)


#Compara IMC do utilizador com IMC tabelado

if IMC < 18.5:
    print(f"O seu IMC é de {IMC}. Você está Abaixo do peso.")
elif 18.5 <= IMC < 24.9:
    print(f"O seu IMC é de {IMC}. Você está com Peso Normal.")
elif 25 <= IMC < 29.9:
    print(f"O seu IMC é de {IMC}. Você está com Sobrepeso.")
elif 30 <= IMC < 34.9:
    print(f"O seu IMC é de {IMC}. Você está com Obesidade Grau I.")
elif 35 <= IMC < 39.9:
    print(f"O seu IMC é de {IMC}. Você está com Obesidade Grau II (Severa).")
elif IMC >= 40:
    print(f"O seu IMC é de {IMC}. Você está com Obesidade Grau III (Mórbida).")
    
