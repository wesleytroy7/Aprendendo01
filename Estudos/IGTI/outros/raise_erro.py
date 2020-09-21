idades = {'Tulio': 30, 'Maria':28, 'Antonio': 33}
pessoa = input('Quero saber a idade de :')
idade = idades.get(pessoa) # metodo get busca o nome  na lista idades

""" if idade:
	print(f'{pessoa} tem {idade} anos de idade.')
else:
	print(f"{pessoa} com idade desconhecida.")
 """

try:
	print(f"{pessoa} tem {idades[pessoa]} anos de idade")
except KeyError:
	print(f'{pessoa} com idade desconhecida')

