a=int(input("Digite um numero inteiro:"))
b=int(input("Digite outro numero inteiro:"))

maior=max(a,b)
menor=min(a,b)

soma = 0
for i in range (menor + 1, maior):
    if i % 2 !=0:
        soma+=1
print ("soma dos impares: ", soma)
