# #gerando uma exceção 
# x = 9
# if x > 5:
#     raise Exception('X não deve ser maior que 5')
# print('bla')

#tratando erros de exception
try:
    numerador = int(input("Entre com numerador:"))
except ValueError: #captura apenas exceções do tipo ValueErrors
    print("Você não entrou com um número inteiro!!!")
    exit(0)# sai do programa
try:
    denominador = int(input("Entre com denominador:"))
except ValueError: #Captura apenas exceções do tipo ValuesErrrors
    print("Você não digitou com um numero inteiro!!!")
    exit(0)# sai do programa
try:
    if numerador % denominador == 0:
        print("O numerador e divisivel pelo denominador!!")
    else:
        print("A divisão não é  inteira.")
except ZeroDivisionError : 
    print("Denominador não pode ser zero!!!")
    