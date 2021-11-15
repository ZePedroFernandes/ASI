def acumulado(condutores: dict):
    table = {}

    for num_carta, matriculas in condutores.items():
        if not (num_carta in table.keys()):
            table[num_carta] = 0
        for matricula, multas in matriculas.items():
            for dia, multasArray in multas.items():
                for multa in multasArray:
                    table[num_carta] += float(multa[1])

    return table