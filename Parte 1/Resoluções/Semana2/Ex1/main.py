idades = [16, 18, 10, 28, 24, 26, 30, 46, 72, 65, 91]

idades.sort()

print("Pessoa mais nova", idades[0])
print("Pessoa mais velha", idades[len(idades) - 1])

somaIdades = 0

for idade in idades:
    somaIdades += idade

media = somaIdades / len(idades)
str = "%.2f" % media
print("Média:", str)

somaIdadesAdultos = 0
adultosNumber = 0
for idade in idades:
    if (18 <= idade <= 65):
        somaIdadesAdultos += idade
        adultosNumber += 1

mediaAdultos = somaIdadesAdultos / adultosNumber
strAdultos = "%.2f" % mediaAdultos
print("Media de idade de pessoas entre 18 e 65 anos é ", strAdultos)
