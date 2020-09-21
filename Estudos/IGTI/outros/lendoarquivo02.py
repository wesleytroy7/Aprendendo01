arquivo02 = input("Entre com o nome do aquivo: ")
arquivo = open(arquivo02,"r")
for linhas in arquivo:
    print(linhas.rstrip())# não lÊ o final da linha, linha em branco a tabulação
arquivo.close()