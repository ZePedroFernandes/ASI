string = "8200123;Ana Maria;931221012;12/05/2000"


lista = string.split(";")
print(lista)
print(len(lista))
lista.append("SOL")
print(lista)
joinedList: string = ",".join(lista)
print(joinedList)
