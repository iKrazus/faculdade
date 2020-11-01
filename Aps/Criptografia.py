def crip():
    palavra = input("Digite uma palavra para criptografar: ") #Esse aqui é um teste#
    cripto=' '
    for i in range(0,len(palavra)):
        cripto = cripto+chr(ord(palavra[i])+10)
    print(cripto)

    

def descrip():
    palavra = input("Digite uma palavra para criptografar: ")
    descripto=' '
    for i in range(0,len(palavra)):
        descripto = descripto+chr(ord(palavra[i])-10)
    print(descripto)

     

op = 'N'
while op != 3:
    print("\t\t\t Criptografia \n")
    print("Digite '1' para Criptografar")
    print("Digite '2' Descriptografar")
    print("Digite '3' para sair do sistema")
    op = int(input("\n Digite sua opção ou '3' para sair: "))

    if op == 1:
        crip()
    if op == 2:
        descrip()
