import re

nome = "Jose Pedro Fernandes"

pattern = re.compile(r'[A-Z][a-z]*( [A-Z][a-z]*)*')

print(pattern.match(nome))

if pattern.match(nome):
    print("Ok")
else:
    print("Not Ok")
