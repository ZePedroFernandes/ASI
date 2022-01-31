def ageAverage(students):
    if len(students) == 0:
        return 0

    ages_sum = 0
    for value in students.values():
        ages_sum = ages_sum + int(value[2])
    return ages_sum / len(students)


students = {}

with open("input.txt") as file:
    for line in file:
        line = line.strip().split(";")
        students[line[0]] = line[1:]

print(ageAverage({}))
