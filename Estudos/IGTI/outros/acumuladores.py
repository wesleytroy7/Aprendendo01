'''
#contando a qdt de elementos inteiros que existem em uma lista
string_inteiros=input("Entre com uma lista de inteiros. ")
lista_inteiros=string_inteiros.split()
contador = 0 # aqui definimos o nosso acumulador e inicializamos a  contagem
for inteiro in lista_inteiros:
    contador=contador+1
print("Existem %.d inteiros na lista" % contador)
'''

'''
n=int(input("Entre com um numero não negativo: "))
fatorial=1
for i in range(1,n+1):
    fatorial=fatorial*1
print(str(n)+"! = ",fatorial)
'''
'''
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
soma = 0
for numero in lista_numeros:
    soma = soma + numero
print(soma)
'''
condicao = 10
soma = 1
while soma <= condicao:
    print("Está é a {}ª vez que entro no loop. ".format(soma))
    soma = soma +1

