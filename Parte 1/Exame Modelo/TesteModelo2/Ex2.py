import re

nome = "Luis Corte-Real Sousa"

pattern = re.compile(r'[A-Z]')
result = pattern.findall(nome)

for letra in result:
    print(str(letra).lower(), end=".")

