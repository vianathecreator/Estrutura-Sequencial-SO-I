n=int(input("DIGITE UM NUMERO INTEIRO:"))

soma = 1
fatorial = 1

for i in range (1, N + 1):
    fatorial *= i
    soma += 1 / fatorial

print ("Resultado da série: ", soma)
