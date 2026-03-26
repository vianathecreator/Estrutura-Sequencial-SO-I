horainicio=int(input("Hora de inicio: "))
mininicio=int(input("Minuto de inicio: "))
horafim=int(input("Hora de fim: "))
minfim=int(input("Minuto de fim: "))

inicio = (horainicio * 60 + mininicio)
fim = (horafim * 60 + minfim)

if fim >= inicio:
    duracao = fim - inicio
else:
    duracao = (24*60 - inicio) + fim

horas = duracao//60
minutos = duracao % 60

print ("a duração foi de ", horas, "horas e", minutos, "minutos")