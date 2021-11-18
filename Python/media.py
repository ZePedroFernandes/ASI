idades = [16, 18, 10, 28, 24, 26, 30, 46, 72, 65, 91]
idades.sort()
print(idades)

# Método 1

i = 0
while i < len(idades):
    if not (18 <= idades[i] <= 65):
        idades.pop(i)
    else:
        i += 1

print(idades)

sum = 0
num = 0
for idade in idades:
    sum += idade
    num += 1

print("Media metodo 1: %.2f" % (sum / num))

## Método 2

media = idades[0]
idades.pop(0)
for i, idade in enumerate(idades):
    media = media * (i + 1) / (i + 2) + idade / (i + 2)

print("Média metodo 2: %.2f" % media)

"""
16 -> 0  * 0 / 1 + 16 / 1
18 -> 16 * 1 / 2 + 18 / 2 = 17
20 -> 17 * 2 / 3 + 20 / 3 = 18

n = 0...len
v  -> media * (n + 1) / (n + 2) + v / (n + 2)
"""
