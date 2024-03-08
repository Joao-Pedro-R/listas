#ex. 9
preco = float(input("Insira um preço: "))
desconto = int(input("Insira uma porcentagem de desconto (sem o sinal %): "))
print(f"O valor do desconto é: {preco * (desconto / 100)}")
print(f"O novo valor é: {preco - (preco * (desconto / 100))}")