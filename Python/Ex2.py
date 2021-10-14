ex2 = "8200123;Ana Maria;931221012;12/05/2000"

splitedList = ex2.split(";")

print(splitedList)
print("This list has", len(splitedList), "elements")
splitedList.append("SOL")
print(splitedList)
commaJoinedList = str(",".join(splitedList))
