def ler(file: str):
    URL = {}
    with open(file) as dataFile:
        for line in dataFile:
            info_list = line.strip().split(";")

            # get info
            url = info_list[0]
            date = info_list[1]
            country = info_list[2]
            time = info_list[3]

            if not (url in URL.keys()):
                URL[url] = {date: [(country, getSecs(time))]}
            else:
                if not(date in URL[url].keys()):
                    URL[url][date] = [(country, getSecs(time))]
                else:
                    URL[url][date].append((country, getSecs(time)))

    return URL


def getSecs(time: str):
    values = time.split(":")
    secs = (int(values[2])) + int(values[1]) * 60 + int(values[0]) * 60 * 60
    return secs
