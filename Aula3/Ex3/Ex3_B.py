Students = {}

with open("input.txt") as file:
    for line in file:
        info = line.strip().split(";")
        Students[info[0]] = info[1:]

inputNumber = None
print("To exit input 0")
while inputNumber != "0":
    inputNumber = input("Student Number to Search:")
    if inputNumber != "0":
        if inputNumber in Students.keys():
            print(Students[inputNumber])
        else:
            print("Student not found!")
