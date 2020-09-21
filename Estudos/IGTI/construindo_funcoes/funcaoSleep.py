from time import sleep

def processando_dados(data):
    print("Iniciando o processamento de algum dado ....")
    modificando_dado = data + " o dado foi modificado!!"
    sleep(2)
    print("Processamento do dado terminado.")
def lendo_dado_from_web():
    print("Lendo dados da Web")
    data = "Dados da web lidos"
    return data 
def  escrevendo_dado_no_DB(data):
    print("Armazenando dados em um DB")
    print(data)
def main():
    data = lendo_dado_from_web()
    modificando_dado=processando_dados(data)
    escrevendo_dado_no_DB(modificando_dado)
if __name__ == "__main__":
    main()