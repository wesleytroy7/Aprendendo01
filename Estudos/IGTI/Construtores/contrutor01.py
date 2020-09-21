#criando uma classe carro
class Carro:
    def __init__(self,numero_portas,preco):# __init__ é o construtor da classe
        self.numero_portas = numero_portas
        self.preco = preco
        print("Obj carro instanciado com sucesso.")
    def get_numero_portas(self):
        return self.numero_portas # self retorna especificamente o valor 

carro_01 = Carro(4,50000)

portas_carro_01 = carro_01.get_numero_portas()
print("Meu carro possui %d portas." %portas_carro_01)

carro_02 = Carro(2, 80000)
portas_carro_02 = carro_02.get_numero_portas()

print("O Carro 02 possui %d portas." %portas_carro_02)

print("Endeço em memoria do carro 01: ", hex(id(carro_01)))
print("Endeço em memoria do carro 02: ", hex(id(carro_02)))