import json

obj = {}

with open("input.txt") as file:
    for line in file.readlines():
        info = line.strip().split(";")
        numero = info[0]
        nome = info[1]

        obj[numero] = info[1]

print(json.dumps(obj, indent=2))

numero = input("Digite um numero:")

if numero in obj.keys():
    print(numero, obj[numero])
else:
    print("Aluno não encontrado")
