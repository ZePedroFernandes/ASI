import math
import re

string = "Smoked Turkey Sandwich: $4.5001"


def toEur(targetString: str):
    pattern = re.compile(r'(.*)\$(\d+\.\d+)$')
    result = pattern.match(targetString)
    descricao = result.group(1)
    dolares = result.group(2)
    eurPrice = "%.3f" % (0.8182 * float(dolares))
    return descricao + "€" + eurPrice[0:(len(eurPrice) - 1)]


print(toEur(string))
