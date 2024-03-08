#ex. 14

vista = float(input("Insira o valor total a vista: "))
parcela = float(input("Insira o valor de parcela que quer pagar: "))
if (parcela * 10) != vista:
    print("ERRO") 
somatoria = 0
i = 0
while True:
    parcela = parcela * 1.01
    somatoria += parcela
    i += 1
    if i == 10:
        break
    else:
        continue

print(f"Total parcelado: {somatoria:.2f} reais")
print(f"Houve um aumento de {(somatoria * 100 / vista) - 100:.2f}%")
