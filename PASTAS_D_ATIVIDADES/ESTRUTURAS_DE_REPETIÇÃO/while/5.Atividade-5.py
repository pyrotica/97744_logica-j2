import os
os.system("cls || clear")
print("""
==========================MENU==========================

CODIGO:                   RESULTADO:

   1 -                    CONTINUAR 
   2 -                    MENSAGEM
   3 -                      SAIR
  """)
opcao = 0
while True:
    

    opcao = str(input("Digite a opçãp: "))
    
    if opcao == '1':
         print("Você escolheu continuar.")
    elif opcao == '2':
         print("Esta é a mensagem que você pediu!")
    elif opcao == '3':
         print("Saindo do programa...")
         break
    else:
          print("Opção inválida. Tente novamente.")