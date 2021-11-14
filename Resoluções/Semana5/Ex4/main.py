import re


def verificarNome(nome: str):
    pattern = re.compile(r'[A-Z][a-z]+( [A-Z][a-z]+)+')
    return bool(pattern.match(nome))


print(verificarNome("Jose Pedro Fernandes"))
