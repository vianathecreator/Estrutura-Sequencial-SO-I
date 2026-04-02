voltas=int(input("Digite o numero de voltas: "))
circuito=float(input("Digite a extensão do circuito em metros: "))
duracao=float(input("Digite a duração da viagem em minutos: "))

km=(voltas*circuito)/1000
tempo=duracao/60
velocidade=km/tempo
print(f"A velocidade média foi de {velocidade:.2f} km/h")
