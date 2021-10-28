data = {}

with open("dados.txt") as file:
    for line in file:
        info = line.strip().split((";"))
        if not (info[0] in data.keys()):
            data[info[0]] = {info[1]: info[2]}
        else:
            data[info[0]][info[1]] = info[2]

inputNif = input("Insira um NIF:")
if inputNif in data.keys():
    for item, value in data[inputNif].items():
        print("Matricula:", item, "\t", "IUC:", value)

else:
    print("NIF not found!")
