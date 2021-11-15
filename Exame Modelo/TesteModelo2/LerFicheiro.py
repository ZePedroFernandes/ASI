def ler(fileName: str):
    alunos = {}
    nomeAlunos = {}
    with open(fileName) as file:
        for line in file.readlines():
            info = line.strip().split(";")
            uc = info[0]
            numAluno = info[1]
            nomeAluno = info[2]
            nota = info[3]

            if not (numAluno in alunos.keys()):
                alunos[numAluno] = {uc: nota}
            else:
                alunos[numAluno][uc] = nota

            if not (numAluno in nomeAlunos.keys()):
                nomeAlunos[numAluno] = nomeAluno

    return alunos, nomeAlunos

