import os
os.system("cls || clear")
print("""
==========================MENU==========================

CODIGO:                   RESULTADO:

   1 -                    CONTINUAR 
   2 -                    MENSAGEM
   3 -                      SAIR
  """)
print()
opcao = 0
while True:
    
    print()
    opcao = str(input("Digite a opçãp: "))
    
    if opcao == '1':
         print()
         print("Você escolheu continuar.")
         
    elif opcao == '2':
         print()
         print("Mensagem :V")
         
    elif opcao == '3':
         print()
         print("Saindo do programa...")
         
         break
    else:
          print()
          print("Opção inválida. Tente novamente.")