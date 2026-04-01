diaat=int(input("Digite o dia atual:"))
mesat=int(input("Digite o mes atual:"))
anoat=int(input("Digite o ano atual:"))

dianasc=int(input("Digite o dia de nascimento:"))
mesnasc=int(input("Digite o mes de nascimento:"))
anonasc=int(input("Digite o ano de nascimento:"))

if diaat < dianasc:
    mesat -= 1
if mesat == 0:
    mesat = 12
    anoat -= 1

if mesat in [1, 3, 5, 7, 8, 10, 12]:
    diasmes=31
elif mesat in [4,6,9,11]:
    diasmes=30

if (anoat % 4 == 0 and anoat % 100 !=0) or (anoat % 400 == 0):
    diasmes = 29
else:
    diasmes=28

diaat += diasmes

dias = diaat - dianasc

if mesat < mesnasc:
    mesat += 12
    anoat -= 1

meses= mesat - mesnasc
anos = anoat - anonasc

print (f"{anos} anos, {meses} meses, {dias} dias")