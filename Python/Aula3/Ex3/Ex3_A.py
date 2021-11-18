import json

feminineStudents = {}

with open("input.txt") as file:
    for line in file:
        info = line.strip().split(";")
        if info[2] == "F":
            feminineStudents[info[0]] = info[1:]

inputNumber = None
print("To exit input 0")
while inputNumber != "0":
    inputNumber = input("Student Number to Search:")
    if inputNumber != "0":
        if inputNumber in feminineStudents.keys():
            print(feminineStudents[inputNumber])
        else:
            print("Student not found!")
