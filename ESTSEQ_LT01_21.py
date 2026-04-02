nota1=float
nota2=float
nota3=float
nota4=float
media=float

nota1=float(input("Digite a nota do primeiro bimestre: "))
nota2=float(input("Digite a nota do segundo bimestre: "))
nota3=float(input("Digite a nota do terceiro bimestre: "))
nota4=float(input("Digite a nota do quarto bimestre: "))
media = ((nota1 + nota2 + nota3 + nota4) / 4)
if (media >= 6.0):
    print ("Aprovado!")
elif (media >= 3.0) and (media < 6.0):
    print ("Recuperação")
else:
    print ("Retido!")
