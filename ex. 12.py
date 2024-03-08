#ex. 12

rm = int(input("Insira o seu rm: "))
if rm >= 100000 or rm <= 9999:
    print("O RM tem 5 dígitos.")
    quit()
somatoria = 0

resto1 = rm % 10
somatoria += resto1
n1 = rm // 10
resto2 = n1 % 10
somatoria += resto2
n2 = n1 // 10
resto3 = n2 % 10
somatoria += resto3
n3 = n2 // 10
resto4 = n3 % 10
somatoria += resto4
n4 = n3 // 10
resto5 = n4 % 10
somatoria += resto5


print(somatoria)


