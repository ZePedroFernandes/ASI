def getAgeGroup(age: int):
    if age <= 12:
        return "Child"
    if age <= 17:
        return "Teenager"
    if age <= 64:
        return "Adult"
    return "Senior"


data = "18/08/1800"

personAge = 2021 - int(data.split('/')[2])

print("This person age group is", getAgeGroup(personAge))
