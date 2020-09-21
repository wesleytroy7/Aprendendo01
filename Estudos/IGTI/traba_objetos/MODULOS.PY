import sys, datetime, platform,math

print(sys.path)# Apresenta os locais onde o python vai pesquisar os modulos


print(datetime.datetime.now())# modulo utilizado para monitorar a plataforma (S.O) que estamos utilizando

x = platform
platform = x.system()
print(platform)
print(x.python_version())
print(x.processor())

conteudo = dir(math)
print(conteudo)


