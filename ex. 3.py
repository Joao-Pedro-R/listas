# 3. Escreva um algoritmo que recebe o nome de uma pessoa e seu ano de nascimento. 
#Seu algoritmo deverá mostrar na tela o nome da pessoa e a idade que ele tem ou terá até o fim de 2024. 
#Por exemplo, supondo que a pessoa informe o ano de nascimento como 1986 seu programa deverá imprimir: Fulano de tal tem (ou terá) 34 anos

nome03 = input("Insira o seu nome: ")
sobrenome03 = input("Insira o seu sobrenome: ")
Ano03 = input("Insira o ano que você nasceu: ")
Idade = 2024 - int(Ano03)
print(f"{nome03} {sobrenome03} tem (ou terá) {Idade} anos em 2024.")
