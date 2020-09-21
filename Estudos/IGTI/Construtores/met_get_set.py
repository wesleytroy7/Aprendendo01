# Importado o modulo array
import array as ar 
# inicializando o array
meu_array = ar.array('i',[2,2,3,2,2,7])

#print do array
print(meu_array)

# Acessando  o indice do valor igual a 2
print(meu_array.index(2))# Apresenta o em qual posição do array está o valor informado, ele para de procurar quando encontra o primeiro valor igual ao que foi informado

# Acessando a quantidade de valores 2 existentes
print(meu_array.count(2))# conta quantos valores existem que são iguais ao que foi informado

class Carro:
    def __init__(self,num_ports,preco):
        self.num_ports = num_ports
        self.preco = preco
        print("Obj criado com sucesso.!!!")
    def get_num_portas(self):
        return self.num_ports
    def set_num_portas(self,novo_num_portas):
        self.num_ports = novo_num_portas


carro_03 = Carro(6, 600000)
print("Numero de portas antes :",carro_03.get_num_portas()) # metodo get - não modifica o estado do Obj
carro_03.set_num_portas(2)# Modifica o numero de portas
print("Novo Numero de portas :",carro_03.get_num_portas())
    