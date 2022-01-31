import re

expressao = "5+-172+5-5/2*5"

pattern = re.compile(r'^(-?\d+)((\+|-|/|\*)((\d+)|\(-\d+\)))*$')

resultado = pattern.match(expressao)

if resultado:
    print("Ok:", eval(expressao))
else:
    print("NOK")
