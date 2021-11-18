def listagem(notasAlunos: dict, nomeAlunos:dict):
    alunosAprovados = []

    for numero, notas in notasAlunos.items():
        if 'ASI' in notas.keys():
            nota = int(notas['ASI'])
            if nota >= 10:
                alunosAprovados.append(nomeAlunos[numero])

    return alunosAprovados
