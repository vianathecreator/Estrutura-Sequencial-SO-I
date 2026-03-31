print ("1 - POUPANÇA")
print ("2 - RENDA FIXA")
escolha=int(input("Escolha uma opção: "))
if (escolha == 1):
    valor=int(input("Digite o valor: "))
    poupanca = valor * 1.03
    print (f"Seu valor depois de um mês é de {poupanca:.2f}")
else:
    valor=int(input("Digite o valor: "))
    poupanca = valor * 1.05
    print (f"Seu valor depois de um mês é de {poupanca:.2f}")
