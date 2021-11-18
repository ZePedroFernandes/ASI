import datetime
import re

diaAtual = datetime.date.today().day
mesAtual = datetime.date.today().month
anoAtual = datetime.date.today().year

print("Hoje é", datetime.date.today())

data = "14/12/2001"

pattern = re.compile(r'\d+')
match = pattern.findall(data)
dia = int(match[0])
mes = int(match[1])
ano = int(match[2])
print("-".join([str(dia), str(mes), str(ano)]))

idade = anoAtual - ano

if (mesAtual < mes) or (mesAtual == mes and diaAtual < dia):
    idade -= 1

print(idade)

classificacao = ""
if idade < 13:
    classificacao = "criança"
elif idade < 18:
    classificacao = "juvenil"
elif idade < 64:
    classificacao = "adulto"
else:
    classificacao = "senior"

print(classificacao)
