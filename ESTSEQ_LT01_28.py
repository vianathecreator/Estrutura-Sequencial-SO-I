precoat=float(input("Digite o preço atual do produto: "))
media=float(input("Digite a média mensal do produto: "))

if (media < 500) and (precoat < 30):
    preco = (precoat * 1.10)
elif (media>=500) and (media<1000) and precoat >=30 and precoat <80:
    preco = (precoat * 1.15)
elif (media>=1000) and (media>=80):
    preco = (precoat * 0.95)
else:
    preco = precoat

print(f"Novo preço: R$ {preco:.2f}")
