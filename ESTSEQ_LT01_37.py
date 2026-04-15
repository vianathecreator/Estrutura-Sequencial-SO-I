n=int(input("DIGITE UM NUMERO INTEIRO:"))

a=0
b=1

for i in range (n):
    print (a, end=" ")
    proximo = a + b
    a = b
    b = proximo