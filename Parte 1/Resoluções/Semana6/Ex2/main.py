
with open("dados.txt") as file:
    for line in file.readlines():
        line.strip()
        info = line.split(";")
        nome = info[0]
        idade = int(info[1])

        if idade < 18:
            print(nome, idade, "menor de idade")
        elif idade < 65:
            print(nome, idade, "maior de idade")
        else:
            print(nome, idade, "senior")
