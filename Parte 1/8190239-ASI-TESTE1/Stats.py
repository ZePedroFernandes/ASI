def topPrecipitacao(table: dict):
    precipitacaoTable = {}
    for distrito, mesano in table.items():
        if not (distrito in precipitacaoTable.keys()):
            precipitacaoTable[distrito] = 0

        for info in mesano.values():
            precipitacaoTable[distrito] += int(info["precipitacao"])

    maiorDistrito = ""
    maiorPrecipitacao = 0

    for distrito, precipitacao in precipitacaoTable.items():
        if precipitacao > maiorPrecipitacao:
            maiorDistrito = distrito
            maiorPrecipitacao = precipitacao

    return maiorDistrito, str(maiorPrecipitacao)


def minTemp(table: dict):
    minTemperatura = float("inf")
    minTemperaturaMes = ""

    for info in table.values():
        for mes, dadosMeteorologicos in info.items():
            temperatura = int(dadosMeteorologicos["temperatura"])
            if minTemperatura > temperatura:
                minTemperatura = temperatura
                minTemperaturaMes = mes

    return minTemperaturaMes, str(minTemperatura)

