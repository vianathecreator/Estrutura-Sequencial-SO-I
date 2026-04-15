numeros = []

for i in range(5):
            num=int(input(f"Digite o {i+1}o número: "))
            numeros.append(num)

menor=min(numeros)
maior=max(numeros)
print("O menor número é: ", menor)
print("O maior número é: ", maior)