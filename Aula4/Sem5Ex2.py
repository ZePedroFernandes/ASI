import re

text = """Jose Antonio;22;M;961237272
Maria Joaquina;30;F;911238981
Joao Melres;35;M;921234240
Ana Rita;25;F;938763310
Ana Raquel;30;F;938763320"""

mPattern = re.compile(r'(?P<nome>[A-Za-z]* [A-Za-z]*);(?P<idade>\d*);M;(?P<tel>\d{9})')
fPattern = re.compile(r'(?P<nome>[A-Za-z]* [A-Za-z]*);(?P<idade>\d*);F;(?P<tel>\d{9})')

mDicionario = {}
fDicionario = {}

for line in text.splitlines():
    mGroups = mPattern.search(line)
    if mGroups:
        mDicionario[mGroups.group("tel")] = mGroups.group("nome")
        print(mPattern.sub(r"\g<nome>;\g<idade>;M;00351\g<tel>", line))
    else:
        fGroups = fPattern.search(line)
        if fGroups:
            fDicionario[fGroups.group("tel")] = fGroups.group("nome")
            print(fPattern.sub(r"\g<nome>;\g<idade>;F;00351\g<tel>", line))

