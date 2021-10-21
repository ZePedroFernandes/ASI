ages = [16, 18, 10, 28, 24, 26, 30, 46, 72, 65, 91]

younger = ages[0]
oldest = ages[0]
adultsSum = 0
adultsNo = 0

for i in range(1, len(ages)):
    if ages[i] < younger:
        younger = ages[i]
    else:
        if ages[i] > oldest:
            oldest = ages[i]
    if 18 <= ages[i] <= 65:
        adultsSum += ages[i]
        adultsNo += 1

print("The younger age is", younger)
print("The oldest age is", oldest)
print("Mean age is", "%.2f" % (sum(ages)/len(ages)))
print("Adult Mean age is", "%.2f" % (adultsSum/adultsNo))
