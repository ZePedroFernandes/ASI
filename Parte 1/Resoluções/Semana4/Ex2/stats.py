def URLmaisVisitado(URL: dict):
    mostVisitedURL = ""
    timesVisited = 0
    for url, dateURL in URL.items():
        tmp = 0
        for date, visits in dateURL.items():
            tmp += len(visits)
        if tmp > timesVisited:
            mostVisitedURL = url
            timesVisited = tmp

    return mostVisitedURL


def mesMaisVisitado(URL: dict):
    months = [0] * 12
    mostVisitedMonth = -1
    mostVisits = 0

    for url, dateURL in URL.items():
        tmp = 0
        for date, visits in dateURL.items():
            mes = int(str(date).split("/")[1]) - 1
            months[mes] += len(visits)

    for month, visits in enumerate(months):
        if visits > mostVisits:
            mostVisitedMonth = month
            mostVisits = visits

    match mostVisitedMonth:
        case 0:
            return "Janeiro"
        case 1:
            return "Fevereiro"
        case 2:
            return "Março"
        case 3:
            return "Abril"
        case 4:
            return "Maio"
        case 5:
            return "Junho"
        case 6:
            return "Julho"
        case 7:
            return "Agosto"
        case 8:
            return "Setembro"
        case 9:
            return "Outubro"
        case 10:
            return "Novembro"
        case 11:
            return "Dezembro"


def TIMEURLmaisVisitado(URL: dict):
    array = []
    finalArray = []
    for url, dateURL in URL.items():
        tmp = 0
        for date, visits in dateURL.items():
            time = 0
            for visit in visits:
                timearray = str(visit[1]).split(":")
                hours = int(timearray[0]) * 60 * 60
                minutes = int(timearray[1]) * 60
                seconds = int(timearray[2])
                time += hours + minutes + seconds
            dateArray = str(date).split("/")
            month = int(dateArray[1])
            year = int(dateArray[2])
            array.append((url, year, month, time))

    while len(array) != 0:
        nextPosition = 0
        i = 1
        for item in array[1::]:
            if item[1] < array[nextPosition][1]:  # ano menor
                nextPosition = i
            elif item[1] == array[nextPosition][1]:  # ano igual
                if item[2] < array[nextPosition][2]:  # mes menor
                    nextPosition = i
                elif (item[2] == array[nextPosition][2]) and (item[3] < array[nextPosition][3]):  # mes igual e tempo menor
                    nextPosition = i

            i += 1
        finalArray.append(array[nextPosition])
        array.pop(nextPosition)

    return finalArray

