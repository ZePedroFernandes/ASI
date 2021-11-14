import re

def numeroMinusculas(targetString: str):
    pattern = re.compile(r'[a-z]*')
    stringSemMinusculas = pattern.sub("", targetString)
    return len(targetString) - len(stringSemMinusculas)


print(numeroMinusculas("aaaaaAAA"))
