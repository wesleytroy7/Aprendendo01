#construtor de uma classe
class Carro:
    def __init__(self,cor='Verm',n_portas=3):#__init__ indica o construtor da class,self utilizada para referenciar os atributos e metodos da classe
        self.cor_carro=cor
        self.n_portas_carro=n_portas

    def get_cor_do_carro(self):
        return self.cor_carro

    def get_num_portas(self):
        return self.n_portas_carro

