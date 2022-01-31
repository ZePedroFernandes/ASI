def URLmaisVisitado(url: dict):
    most_visited_url = []
    most_visited_url_visits = 0

    for key, dates in url.items():
        url = key
        dates = dict(dates)
        url_visits = 0
        for value in dates.values():
            url_visits = url_visits + len(value)

        if url_visits > most_visited_url_visits:
            most_visited_url = [url]
            most_visited_url_visits = url_visits
        elif url_visits == most_visited_url_visits:
            most_visited_url.append(url)

    return most_visited_url


def MESmaisVisitado(url: dict):
    meses = [0] * 12

    for dates in url.values():
        dates = dict(dates)
        # print(dates)
        for date, values in dates.items():
            # print("\t", date, len(values))
            date = str(date)
            mes = int(date.split("/")[1]) - 1
            meses[mes] = meses[mes] + len(values)

    # print(meses)
    mes_mais_visitado = 0
    visitas = meses[mes_mais_visitado]
    for i in range(1,12):
        if meses[i] > visitas:
            mes_mais_visitado = i
            visitas = meses[i]

    return getMes(mes_mais_visitado + 1)

def getMes(number: int):
    match number:
        case 1:
            return "Janeiro"
        case 2:
            return "Fevereiro"
        case 3:
            return "Março"
        case 4:
            return "Abril"
        case 5:
            return "Maio"
        case 6:
            return "Junho"
        case 7:
            return "Julho"
        case 8:
            return "Agosto"
        case 9:
            return "Setembro"
        case 10:
            return "Outubro"
        case 11:
            return "Novembro"
        case 12:
            return "Dezembro"

def TIMEURLmaisVisitado(URL: dict):
    return 0