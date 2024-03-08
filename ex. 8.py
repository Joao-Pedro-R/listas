#ex. 8

nome = input("Insira o seu nome: ")
camisas = int(input("Insira o número de camisas que possui: "))
calcas = int(input("Insira o número de calças que possui: "))
sapatos = int(input("Insira o número de pares de sapato que possui: "))
print(f"{nome} possui {camisas} camisas.")
print(f"{nome} possui {calcas} calças.")
print(f"{nome} possui {sapatos} pares de sapato.")
print(f"{nome} possui {camisas * calcas * sapatos} combinações de roupas possíveis.")