def media(notasAlunos: dict):
    disciplinas = {}
    for numero, notas in notasAlunos.items():
        for uc, nota in notas.items():
            if not (uc in disciplinas):
                disciplinas[uc] = [int(nota), 1]
            else:
                soma = disciplinas[uc][0]
                tmp = disciplinas[uc][1] + 1
                disciplinas[uc] = [soma, tmp]

    for uc, array in disciplinas.items():
        disciplinas[uc] = disciplinas[uc][0] / disciplinas[uc][1]

    return disciplinas
