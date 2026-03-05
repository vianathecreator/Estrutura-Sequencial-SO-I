#declaraçao variavel
A = int
B = int 
C = int
delta = int
x1 = int
x2 = int

#inicio
A = int (input("Digite o valor de A: "))
B = int (input("Digite o valor de B: "))
C = int (input("Digite o valor de C: "))
delta = (B * B) - (4 * A * C)
x1 = (-B + (delta **0.5)) /(2*A)
x2 = (-B - (delta **0.5)) /(2*A)
print ("Essa é a primeira raiz: ",x1)
print ("Essa é a segunda raiz: ", x2)
#fim