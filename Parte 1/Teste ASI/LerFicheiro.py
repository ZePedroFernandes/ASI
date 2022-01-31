def ler(fileName: str):
    table = {}
    with open(fileName) as file:
        for line in file.readlines():
            info = line.strip().split(";")
            distrito = info[0]
            mesano = info[1]
            precipitacao = info[2]
            temperatura = info[3]
            if not (distrito in table.keys()):
                table[distrito] = {}

            table[distrito][mesano] = {
                "precipitacao": precipitacao,
                "temperatura": temperatura
            }

    return table

