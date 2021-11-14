def ler(fileName: str):
    URL = {}
    with open(fileName) as file:
        for line in file.readlines():
            info = line.strip().split(";")
            url = info[0]
            data = info[1]
            pais = info[2]
            duracao = info[3]

            if not (url in URL.keys()):
                URL[url] = {data: [(pais, duracao)]}
            else:
                if not (data in URL[url].keys()):
                    URL[url][data] = [(pais, duracao)]
                else:
                    URL[url][data].append((pais, duracao))
    return URL
