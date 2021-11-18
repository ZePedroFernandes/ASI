import re


def adicionaDados(fileName: str):
    pattern = re.compile(r'(?P<nota>\d+)$')

    with open(fileName) as file:
        for line in file.readlines():
            line = line.strip()
            result = pattern.search(line)
            tmp = pattern.sub(r'\g<nota>.0', line)
            print(tmp)
