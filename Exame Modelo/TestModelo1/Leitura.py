def ler(fileName: str):
    condutores = {}
    with open(fileName) as file:
        for line in file.readlines():
            info = line.strip().split(";")
            num_carta = info[0]
            matricula = info[1]
            data = info[2]
            contra_ordenacao = info[3]
            coima = info[4]
            data_pagamento = info[5]

            if not (num_carta in condutores.keys()):
                condutores[num_carta] = {matricula: {data: [(contra_ordenacao, coima, data_pagamento)]}}
            else:
                if not (matricula in condutores[num_carta].keys()):
                    condutores[num_carta][matricula] = {data: []}

                condutores[num_carta][matricula][data].append((contra_ordenacao, coima, data_pagamento))
    return condutores
