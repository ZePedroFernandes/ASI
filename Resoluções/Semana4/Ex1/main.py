import re

# precoFinal = "(100*23%)-10%"
#
# pattern = re.compile(r'^(?P<expr>.+)%(?P<expr2>.+)%$')
#
# precoFinal = pattern.sub(r"\g<expr>/100\g<expr2>", precoFinal)
#
# print(precoFinal)
#################################################################
precoFinal = "(100*23%)-10"

pattern = re.compile(r'%')
precoFinal = pattern.sub('/100', precoFinal)
print(eval(precoFinal))
