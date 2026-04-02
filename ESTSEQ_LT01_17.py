#declaraçao de variaveis
tempo=float
vmedia=float
distancia=float
litros=float

#inicio
tempo=float(input("digite o tempo de percurso em horas: "))
vmedia=float(input("digite a velocidade media de km por hora: "))
distancia = tempo * vmedia
litros= distancia/12
print("esse é o numero de litros que sera gasto durante a viagem: ", litros)
#fim
