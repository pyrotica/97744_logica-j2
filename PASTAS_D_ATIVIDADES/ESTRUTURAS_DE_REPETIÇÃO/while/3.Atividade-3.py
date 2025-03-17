import os
os.system("cls || clear")

soma = 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        print(f"zero inserido, a soma total dos números inseridos é: {soma}")
        break
    else:
        soma += numero
        print(f" Valor atual da soma: {soma}")