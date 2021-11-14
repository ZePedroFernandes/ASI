import re

finalString = ""

pattern = re.compile(r'(.+);(.+);(.+);(.+)')

with open("dados.txt") as file:
    for line in file.readlines():
        result = pattern.sub(r'\1;\2;\3;00351\4', line)
        finalString += result

print(finalString)
