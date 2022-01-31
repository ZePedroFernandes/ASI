import json

import LerFicheiro
import Stats

table = LerFicheiro.ler("temp.txt")
print(json.dumps(table, indent=2))

tmp = Stats.topPrecipitacao(table)
print(tmp[0], ":", tmp[1])

tmp2 = Stats.minTemp(table)
print(tmp2[0], ":", tmp2[1])
