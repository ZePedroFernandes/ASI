import re

preco_base = input("Digite o preço base:")
equation = "("+preco_base+"*23%)-10"

pattern = re.compile(r'%')
lista = pattern.search(equation)
equation = pattern.sub("/100", equation)
print(eval(equation))
