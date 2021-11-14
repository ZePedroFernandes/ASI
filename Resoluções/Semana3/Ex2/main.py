import json
import re

nifTable = {}
string = """123456789;12-AZ-21;35.00
134676523;34-NU-24;45.00"""
pattern = re.compile(r'^(?P<nif>.+);(?P<matricula>.+);(?P<IUC>.+)$')

with open("dados.txt") as file:
    for line in file.readlines():
        line = line.strip()
        info = pattern.search(line).groups()
        print(info)
        nif = info[0]
        matricula = info[1]
        IUC = info[2]
        if not (nif in nifTable.keys()):
            nifTable[nif] = {matricula: IUC}
        else:
            nifTable[nif][matricula] = IUC

print(json.dumps(nifTable, indent=2))
