dictionary = {
    "filme": ["film", "movie"],
    "locomotiva": ["locomotive", "train"],
    "pessoa": ["person", "individual"]
}

print("As traduções possíveis para \"locomotiva\" são", "\"" + dictionary["locomotiva"][0] + "\"", end="")

for index in range(1, len(dictionary["locomotiva"])):
    if index is len(dictionary["locomotiva"]) - 1:
        print(" and", end=" ")
    else:
        print(",", end=" ")

    print("\"" + dictionary["locomotiva"][index] + "\"", end="")

