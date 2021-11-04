import re

texto = "Este Texto Tem 23 Letras Minúsculas"

totalSize = len(texto)

pattern = re.compile(r'[A-Z1-9 ]*')

onlyLowerCaseText = pattern.sub("", texto)

print(onlyLowerCaseText)
print("Lower case letters number is:", len(onlyLowerCaseText))
