def soSeparando():
    print(20 * '**')


def  concatena_arg01(nome, msg):
    print("Olá,", nome + '!' + msg)

concatena_arg01("Wesley", "Bom dia") # passando parêmetros,mas se faltar um dá erro 

soSeparando()

def concatena_arg02(nome,msg2 = 'ARIBÁ'):# passando um parâmetro e mantendo outro como padrão
    print("Olá,", nome + '!'+msg2)
concatena_arg02("Wesley")
concatena_arg02("Wes", "Tarde sô!!")

soSeparando()

def argumentos_arbitrarios01(*nomes): #funcao possui N parâmetros
    for osnomes in nomes:
        print("Olá," +osnomes+"! Bom dia!!!")
argumentos_arbitrarios01('Jô','RWE','ttt')

soSeparando()
