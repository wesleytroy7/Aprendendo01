'''
lista_de_compras =[ 'detergente','sabão','amaciante','banana']
item = input("\entre com o produto:")
if item not in lista_de_compras: #se o item não está na lista de compra
    print('{} não consta na lista de compras'.format(item))
else:
    print('Não esqueça de comprar {}.'.format(item))
'''
'''
lista_1 =[1,2,3,4,5,6]
lista_2 = [6,7,8,9]
for Item in lista_1:# in é tipo uma pergunta de busca : o Item está na lista_1?
    if Item in lista_2:
        print(str(Item) + " é comum entre às duas listas.")
    else:
        print(str(Item)+ " não é comum às duas listas")
'''
'''
x = 1
if(type(x) is int):
    print("Verdadeiro")
else:
    print("Falso")
'''
'''
x = 4.5
if(type(x) is not int):
    print("Verdadeiro")
else:
    print("falso")
'''


