import re

info = "Jose Maria Almeida;00351 962341234;1997-11-19"

namePattern = re.compile(r'[A-Z][a-z]+ ([A-Z][a-z]+)+')
phonePattern = re.compile(r'00351 \d{9}')
datePattern = re.compile(
    r'\d+-(((01|03|05|07|08|10|12)-(0[1-9]|1[0-9]|2[0-9]|3[0-1]))|((02)-(0[1-9]|1[0-9]|2[0-9]))|((04|06|09|11)-(0[1-9]|1[0-9]|2[0-9]|30)))')

infoArray = info.split(";")
name = infoArray[0]
phone = infoArray[1]
birth = infoArray[2]

datePattern2 = re.compile(r'(\d+)-(\d+)-(\d+)')

if namePattern.match(name) and phonePattern.match(phone) and datePattern.match(birth):
    birthMatch = datePattern2.match(birth)
    birthYear = int(birthMatch.group(1))
    birthMonth = int(birthMatch.group(2))
    birthDay = int(birthMatch.group(3))
    print(name + ",", phone + ",", birth)
    yearsIn2021 = 2021 - birthYear
    if birthMonth > 11:
        yearsIn2021 -= 1
    elif birthMonth == 11 and birthDay > 15:
        yearsIn2021 -= 1
    print("Em 15-11-2021 terá", yearsIn2021, "anos")
