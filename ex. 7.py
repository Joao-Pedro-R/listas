# 7. Sua tarefa é desenvolver um algoritmo que recebe um número inteiro de 0 a 99
# e imprime o dígito das dezenas e o dígito das unidades desse número. 
# Dica: usando papel e lápis faça a divisão inteira do número por 10 mas não coloque vírgula 
# e nem acrescente 0 na divisão.

while True:
    num07 = int(input("Insira um número entre 0 e 99: "))
    if num07 > 99 or num07 < 0:
        print("LÊ A PORRA DO TEXTO CARALHO.")
    else:
        break

primdig07 = int(num07 // 10)
segdig07 = num07 - (primdig07 * 10)

print(f"{primdig07}, {segdig07}")