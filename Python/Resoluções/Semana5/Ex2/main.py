import re


# b)
def reformatPhoneNumber(phone: str):
    phonepatter = re.compile(r'^')
    return phonepatter.sub('00351', phone)


pattern = re.compile(r'^(?P<nome>.+);(?P<idade>\d+);(?P<genero>[MF]);(?P<numerotelefone>\d{9})$')
masculinos = {}
femininos = {}

with open("dados.txt") as file:
    for line in file.readlines():
        line = line.strip()
        matchResult = pattern.match(line)
        numerotlf = reformatPhoneNumber(matchResult.group('numerotelefone'))
        if matchResult.group('genero') == 'M':
            masculinos[numerotlf] = matchResult.group('nome')
        elif matchResult.group('genero') == 'F':
            femininos[numerotlf] = matchResult.group('nome')


print(masculinos)
print(femininos)
