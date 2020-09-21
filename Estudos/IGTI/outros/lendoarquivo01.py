nome_do_arq = input("insira o nome do arquivo: ")
arquivo = open(nome_do_arq,"r")
for linhas in arquivo:
    print(linhas)
arquivo.close()