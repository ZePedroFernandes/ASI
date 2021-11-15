import json

import Apurar
import Leitura

condutores = Leitura.ler("dados.txt")
apurar = Apurar.acumulado(condutores)

print(apurar)
