import json

alunos = {}

with open("alunos.txt") as file:
    for line in file:
        line = line.strip()
        info = line.split(";")
        alunos[info[0]] = info[1]

print(json.dumps(alunos, indent=2))
number = input("Insira um número")

if(number in alunos.keys()):
    print(alunos[number])
else:
    print("Student not found")