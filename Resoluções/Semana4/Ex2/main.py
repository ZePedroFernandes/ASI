import json

import leitura
import stats

URL = leitura.ler("dados.txt")
urlMaisVisitado = stats.URLmaisVisitado(URL)
mesMaisVisitado = stats.mesMaisVisitado(URL)
time = stats.TIMEURLmaisVisitado(URL)
print("url", "year", "month", "seconds")
for item in time:
    print(item)

