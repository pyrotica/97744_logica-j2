import os
os.system("cls || clear")

soma=0
QUANT_NOTAS=3
for i in range(QUANT_NOTAS):
  while True:
    nota=float(input(f"digite a {i+1}º nota: "))
    print()
    

    if nota< 0 and nota > 10:
       print(f"NOTA INVALIDA")
       print()
       
    else:
       soma += nota
       break

media= soma/QUANT_NOTAS

print(f"soma é {soma}")
print()
print(f"e a sua media aritmetica é: {media:.1f}")
print()
if media >=7:
    print("______________aprovado______________")
    print()
elif media > 5 and media<7:
    print("______________recuperação______________")
    print()
elif media < 5:
    print("______________reprovado______________")
    print()
    
