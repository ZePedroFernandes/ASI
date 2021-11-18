from Leitura import ler
import Stats
import json

URL = ler("dados.txt")
print(json.dumps(URL, indent=2))
