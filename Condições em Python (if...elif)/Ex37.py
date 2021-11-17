num = int(input("Digite um numero: "))
conversor = int(input("Digite uma das Opcoes a Seguir: \n"
                      "[1] converter para BINÁRIO \n"
                      "[2] converter para OCTAL \n"
                      "[3] converter para HEXADECIMAL \n"
                      "Sua opção: "))
if conversor == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif conversor == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif conversor == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("Opção Invalida")


