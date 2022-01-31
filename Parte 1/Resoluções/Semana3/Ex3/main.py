import json


def readStudentsFromFile(fileName: str):
    students = {}
    with open(fileName) as file:
        for line in file.readlines():
            line = line.strip()
            info = line.split(";")
            studentNumber = info[0]
            studentName = info[1]
            studentAge = info[2]
            studentGender = info[3]
            studentPhone = info[4]
            students[studentNumber] = [studentName, studentAge, studentGender, studentPhone]
    return students


def getStudentInfoFromInput(students: dict):
    studentNumber = input("Numero de estudante a pesquisar:")
    if studentNumber in students.keys():
        return students[studentNumber]
    else:
        return []


def getStudentsAverageAge(students: dict):
    studentsAgeSum = 0
    numberOfStudents = 0
    for value in students.values():
        studentsAgeSum += int(value[1])
        numberOfStudents +=1

    averageAge = studentsAgeSum / numberOfStudents
    return averageAge

students = readStudentsFromFile("alunos.txt")
print(students)
print(getStudentsAverageAge(students))
print(getStudentInfoFromInput(students))