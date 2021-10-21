import json

grades = [8, 7, 8, 6, 10, 12, 14, 12, 18, 12, 17]

gradesFrequency = {}

for grade in grades:
    gradesFrequency[grade] = grades.count(grade)

print(json.dumps(gradesFrequency, indent=4))
